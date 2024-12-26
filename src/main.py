import streamlit as st
import pandas as pd
from make_predictions import make_prediction


# Set the page title and layout
st.set_page_config(page_title="What do your biomarkers tell you?", layout="centered")

def apply_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #E3F2FD;  /* Light Blue */
        }
        .stApp {
            background-color: #F5F5F5; /* Light Gray for App Area */
            color: #212121; /* Dark Gray for Text */
        }
        .stButton button {
            background-color: #2196F3; /* Blue Buttons */
            color: #FFFFFF; /* White Text */
            border: none;
            padding: 8px 16px;
            font-size: 16px;
            border-radius: 4px;
            margin: 5px;
        }
        .stButton button:hover {
            background-color: #1976D2; /* Darker Blue on Hover */
        }
        .stMarkdown {
            color: #212121; /* Dark Gray Text for Markdown */
        }
        </style>
    """, unsafe_allow_html=True)

apply_custom_css()

def input_container_style():
    st.markdown("""
        <style>
        .stNumberInput {
            background-color: #F5F5F5;  /* Light Gray */
            border-radius: 4px;
            padding: 5px;
            box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)

input_container_style()

st.markdown("""
    <style>
    div.stButton > button {
        color: white;
        background-color: #2196F3;
        border: none;
        border-radius: 4px;
        padding: 10px 20px;
        font-size: 16px;
        margin: 5px 0;
    }
    div.stButton > button:hover {
        background-color: #1976D2;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#2196F3;'>Diabetes Prediction App</h1>", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #2196F3;'>", unsafe_allow_html=True)



# App header
st.title("What do your biomarkers tell you?")
st.write("Enter your details below to calculate your probability of having diabetes.")

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
            st.markdown(
                f"<div style='background-color:#FF5252;padding:10px;border-radius:5px;color:white;'>"
                f"<b>High Risk!</b> The patient has a {probability[0]:.2%} chance of diabetes.</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='background-color:#4CAF50;padding:10px;border-radius:5px;color:white;'>"
                f"<b>Low Risk!</b> The patient has a {probability[0]:.2%} chance of diabetes.</div>",
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")