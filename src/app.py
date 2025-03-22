import streamlit as st
import numpy as np
from utils import predict_default

# Streamlit UI
st.title("🏦 Loan Approval Predictor - Credit Risk Analysis")
st.write("This app predicts whether a loan applicant is **Approved** or **Rejected** based on financial details.")

# Input fields
income = st.number_input("Applicant Income ($)", min_value=1000, max_value=100000, value=5000, step=100)
credit_history = st.selectbox("Credit History", ["Good", "Bad"])
loan_amount = st.number_input("Loan Amount ($)", min_value=1000, max_value=50000, value=10000, step=500)
employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed"])
marital_status = st.selectbox("Marital Status", ["Married", "Single"])
debt_income_ratio = st.slider("Debt-to-Income Ratio (%)", min_value=0, max_value=100, value=30)

# Prediction button
if st.button("Predict Loan Approval"):
    user_data = {
        "ApplicantIncome": income,
        "Credit_History": credit_history,
        "LoanAmount": loan_amount,
        "Employment_Status": employment_status,
        "Marital_Status": marital_status,
        "Debt_to_Income_Ratio": debt_income_ratio
    }

    prediction = predict_default(user_data)
    
    if prediction == "Approved":
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected!")
