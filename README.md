# AI Investment Recommendation Backend

This is a Flask-based backend for an AI investment recommendation system. It uses a machine learning model to provide personalized investment recommendations based on user inputs.

## Setup

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Train the model:
   ```
   python model.py
   ```
   This will create an `investment_model.pkl` file.

4. Run the Flask server:
   ```
   python app.py
   ```
   The server will run on http://127.0.0.1:5000

## API Endpoints

### POST /predict

Accepts a JSON payload with the following fields:
- `age`: User's age
- `income`: Annual income
- `risk_level`: Risk tolerance level (1-4, where 1 is low risk and 4 is high risk)
- `savings`: Current savings amount
- `investment_goal`: Investment goal type (1-3, where 1 is short-term, 2 is medium-term, 3 is long-term)

Returns:
```json
{
  "recommended_circle": "Investment Circle Name"
}
```

Possible recommendation values: "Conservative", "Balanced", "Growth", "Aggressive" 