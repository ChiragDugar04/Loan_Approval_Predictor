import numpy as np
import pandas as pd
import joblib
from sklearn.impute import SimpleImputer

# Load trained model
MODEL_PATH = "/home/chirag/Loan_approval_predictor/models/lgbm_credit_risk.pkl"
model = joblib.load(MODEL_PATH)

# Load training features
FEATURES_PATH = "/home/chirag/Loan_approval_predictor/models/training_features.npy"
training_features = np.load(FEATURES_PATH, allow_pickle=True)

def preprocess_input(data):
    df = pd.DataFrame([data])

    # Handle missing values
    num_imputer = SimpleImputer(strategy="median")
    df.fillna(num_imputer.fit_transform(df), inplace=True)

    # Align columns with training features
    df = df.reindex(columns=training_features, fill_value=0)

    # Debugging: Check mismatched features
    extra_features = set(df.columns) - set(training_features)
    missing_features = set(training_features) - set(df.columns)

    print("⚠️ Extra features in input:", extra_features)
    print("⚠️ Missing features in input:", missing_features)
    print("Processed input shape:", df.shape)  # Debugging

    return df

def predict_default(user_data):
    processed_data = preprocess_input(user_data)

    if processed_data.shape[1] != len(training_features):
        raise ValueError(f"Feature mismatch! Expected {len(training_features)}, but got {processed_data.shape[1]}.")

    prediction = model.predict(processed_data)[0]
    return prediction
