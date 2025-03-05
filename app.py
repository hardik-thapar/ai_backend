from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load trained model
with open('investment_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[data['age'], data['income'], data['risk_level'], data['savings'], data['investment_goal']]])
    prediction = model.predict(features)
    return jsonify({'recommended_circle': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5001)