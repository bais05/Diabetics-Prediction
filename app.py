import streamlit as st
import numpy as np
import pickle

# load model and scaler
model = pickle.load(open("diabetes_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

st.title("Diabetes Prediction System")

st.write("Enter patient medical details")

# input fields
pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose Level")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin Level")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

# prediction button
if st.button("Predict"):

    input_data = (pregnancies, glucose, blood_pressure, skin_thickness,
                  insulin, bmi, dpf, age)

    input_array = np.asarray(input_data)
    input_reshaped = input_array.reshape(1,-1)

    std_data = scaler.transform(input_reshaped)

    prediction = model.predict(std_data)

    if prediction[0] == 0:
        st.success("The person is NOT diabetic")
    else:
        st.error("The person is diabetic")