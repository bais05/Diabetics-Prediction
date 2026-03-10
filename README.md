# Diabetes Prediction Web App

This project is a Machine Learning based web application that predicts whether a person is diabetic based on medical attributes such as glucose level, BMI, insulin level, age, and blood pressure.

The model is trained using Python and deployed as an interactive web interface using Streamlit.

---

## 🚀 Features

- Predicts diabetes based on patient health parameters
- Interactive web interface
- Real-time prediction
- Machine Learning model trained using Scikit-Learn
- Data preprocessing and feature scaling applied

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling using StandardScaler
4. Model Training (Logistic Regression)
5. Model Evaluation using accuracy, confusion matrix, and precision
6. Deployment using Streamlit

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn
- Streamlit
- Pickle

---

## 📊 Input Features

The model uses the following medical parameters:

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---
## 📁 P
roject Structure

```
Diabetes-Prediction-Streamlit-App
│
├── app.py
├── diabetes_model.pkl
├── scaler.pkl
├── diabetics.csv
├── requirements.txt
└── README.md
```

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/Diabetes-Prediction-Streamlit-App.git
```
Navigate to the project folder:
```bash
cd Diabetes-Prediction-Streamlit-App
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the application:
```bash
streamlit run app.py
```
