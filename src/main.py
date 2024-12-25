import streamlit as st
import pandas as pd
from make_predictions import make_prediction

# Set the page title and layout
st.set_page_config(page_title="Diabetes Prediction App", layout="centered")

# App header
st.title("Diabetes Prediction App")
st.write("Enter patient details below to calculate the probability of diabetes.")

# Input fields
pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0, step=1)
glucose = st.number_input("Plasma Glucose Concentration", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value=0, max_value=200, value=80)
skin_thickness = st.number_input("Triceps Skinfold Thickness (mm)", min_value=0, max_value=100, value=20)
insulin = st.number_input("2-Hour Serum Insulin (mu U/ml)", min_value=0, max_value=800, value=85)
bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=100.0, value=30.0, step=0.1)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
age = st.number_input("Age", min_value=0, max_value=120, value=35, step=1)

# Prediction button
if st.button("Calculate"):
    # Create input DataFrame
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [diabetes_pedigree],
        'Age': [age],
    })

    # Call prediction function
    try:
        prediction, probability = make_prediction(input_data)
        st.success(f"The patient has a {probability[0]:.2%} probability of diabetes.")
        if prediction[0] == 1:
            st.error("The patient is at high risk of having or developing diabetes.")
        else:
            st.success("The patient is at low risk of having or developing diabetes.")
    except Exception as e:
        st.error(f"An error occurred: {e}")