# ❤️ Heart Disease Predictor

An ML-powered web application that predicts the likelihood of heart disease based on patient health data.

## 🖥️ Demo
Enter patient vitals → Get instant risk assessment with probability score.

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

## 🚀 How to Run

**Step 1 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 2 — Run the app**
```bash
python app.py
```

**Step 3 — Open in browser**
```
http://127.0.0.1:5000
```

## 🧠 ML Model
- **Algorithm:** Random Forest Classifier
- **Features used:** Age, Sex, Chest Pain Type, Blood Pressure, Cholesterol, Blood Sugar, Max Heart Rate, Exercise-Induced Angina
- **Accuracy:** ~85%+

## 🛠 Tech Stack
- Python 3
- Flask (web framework)
- Scikit-learn (ML)
- NumPy
- HTML & CSS (frontend)

## ⚠️ Disclaimer
This tool is for **educational purposes only** and is not a substitute for professional medical advice.
