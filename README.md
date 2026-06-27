**❤️ Heart Disease Predictor**

An AI-powered web application that predicts the likelihood of heart disease using patient health parameters. The system integrates a trained Random Forest model with a Flask-based web interface.

**🔍 Project Overview**

This project demonstrates an end-to-end machine learning pipeline:

Synthetic data generation based on real medical risk factors

Random Forest model training and serialization

Flask backend serving predictions

Clean frontend with patient input form and result page

The application is designed to assist in early cardiovascular risk detection by analyzing commonly used clinical indicators.

**⚙️ Features**

Predicts heart disease risk (High Risk / Low Risk)

Shows probability percentage score for each prediction

Clean, responsive, modern UI

Two-page flow: input form → result page

Model auto-trains and saves on first run

**🧠 Machine Learning Model**

The system uses a Random Forest Classifier trained on simulated patient data modeled after real cardiovascular risk patterns.

Input Features:

Age

Sex (Male / Female)

Chest Pain Type (4 categories)

Resting Blood Pressure (mmHg)

Cholesterol Level (mg/dL)

Fasting Blood Sugar (>120 mg/dL)

Maximum Heart Rate Achieved (bpm)

Exercise-Induced Angina

Output:

Binary classification: High Risk / Low Risk

Probability percentage of heart disease risk

Model Performance:

Algorithm: Random Forest Classifier (100 estimators)

Accuracy: ~85%+

## 📁 Project Structure
```
heart-disease-predictor/
├── app.py                  # Flask backend + ML model
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Input form
│   └── result.html         # Prediction result page
└── heart_model.pkl         # Saved model (auto-generated on first run)
```
**🛠️ Tech Stack**

Programming Language: Python

Machine Learning: Scikit-learn (Random Forest)

Backend: Flask

Frontend: HTML, CSS

Version Control: GitHub

 **🚀 How to Run Locally**

 git clone https://github.com/firashashabir/heart-disease-predictor.git
cd heart-disease-predictor
pip install -r requirements.txt
python app.py

Then open:
http://127.0.0.1:5000


**📌 Disclaimer**

This application is intended for educational and demonstration purposes only and should not be used as a substitute for professional medical diagnosis or advice.

**👤 Author**

Firasha Shabir — Student | Machine Learning & AI Enthusiast
GitHub: https://github.com/firashashabir
