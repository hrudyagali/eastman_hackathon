import streamlit as st
import pandas as pd
import joblib 
model=joblib.load("houseprice.pkl")
st.title("house price predictor")
st.write("enter details below")
longitude=st.number_input("longitude")
latitude=st.number_input("latitude")
housing_median_age=st.number_input("housing_median_age")
total_rooms=st.number_input("total_rooms")
population=st.number_input("population")
total_bedrooms=st.number_input("total_bedrooms")
households=st.number_input("households")
median_income=st.number_input("median_income")
ocean_proximity=st.selectbox("ocean_proximity",['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'])
if st.button("predict"):
    model_input=pd.DataFrame([
    {
        'longitude':longitude,
        'latitude':latitude, 
        'housing_median_age':housing_median_age,
          'total_rooms':total_rooms,
       'total_bedrooms':total_bedrooms,
         'population':population,
           'households':households, 
           'median_income':median_income,
       'ocean_proximity':ocean_proximity
    }
])

    prediction=model.predict(model_input)
    st.success(f"prediction is: {prediction} ")