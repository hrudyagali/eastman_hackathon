
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("insurance_model.pkl")

st.title("Medical Insurance Cost Predictor")
st.write("Enter your details to estimate medical insurance charges.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["female", "male"])
bmi = st.number_input(
    "BMI", min_value=10.0, max_value=70.0, value=25.0
)
children = st.number_input(
    "Number of children", min_value=0, max_value=10, value=0
)
smoker = st.selectbox("Smoker?", ["no", "yes"])
region = st.selectbox(
    "Region", ["southwest", "southeast", "northwest", "northeast"]
)

if st.button("Predict Insurance Charges"):
    input_data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated insurance charges: ${prediction:,.2f}")
    st.caption("This is a model estimate for practice, not an actual insurance quote.")
