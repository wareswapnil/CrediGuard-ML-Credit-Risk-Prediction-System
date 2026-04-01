import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("extra_trees_credit_model.pkl")

# Load encoders
encoders = {
    "Sex": joblib.load("Sex_encoder.pkl"),
    "Housing": joblib.load("Housing_encoder.pkl"),
    "Saving accounts": joblib.load("Saving_accounts_encoder.pkl"),
    "Checking account": joblib.load("Checking_account_encoder.pkl")  # FIXED
}

# Title
st.title("Credit Risk Prediction App")
st.write("Enter applicant information to predict whether credit risk is GOOD or BAD")

# Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["male", "female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own", "rent", "free"])
saving_accounts = st.selectbox("Saving accounts", ["little", "moderate", "rich", "quite rich"])
checking_account = st.selectbox("Checking account", ["little", "moderate", "rich"])
credit_amount = st.number_input("Credit amount", min_value=0, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)

# Create DataFrame (FIXED)
sex_map = {"male": 0, "female": 1}

housing_map = {
    "own": 0,
    "rent": 1,
    "free": 2
}

saving_map = {
    "little": 0,
    "moderate": 1,
    "rich": 2,
    "quite rich": 3
}

checking_map = {
    "little": 0,
    "moderate": 1,
    "rich": 2
}

input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [sex_map[sex]],
    "Job": [job],
    "Housing": [housing_map[housing]],
    "Saving accounts": [saving_map[saving_accounts]],
    "Checking account": [checking_map[checking_account]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

# Predict button
if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]

    if pred == 1:
        st.success("The predicted credit risk is: GOOD")
    else:
        st.error("The predicted credit risk is: BAD")