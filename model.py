import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Example dataset (replace with actual data)
data = pd.read_csv('investment_data.csv')

# Features and target
X = data[['age', 'income', 'risk_level', 'savings', 'investment_goal']]
y = data['recommended_circle']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
with open('investment_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Accuracy (optional)
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
