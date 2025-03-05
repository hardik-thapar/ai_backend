from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

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

# Add a simple health check route
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "AI Investment API is running"})

if __name__ == '__main__':
    # Get port from environment variable or default to 5001
    port = int(os.environ.get('PORT', 5001))
    # Bind to 0.0.0.0 to listen on all interfaces
    app.run(host='0.0.0.0', port=port, debug=True)