# ============================================================
#  ❤️ Heart Disease Predictor — Flask Web App
#  ML Model : Random Forest Classifier
#  Run      : python app.py  → open http://127.0.0.1:5000
# ============================================================

from flask import Flask, render_template, request
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# ---------- TRAIN & SAVE MODEL (runs once) ----------
def train_model():
    np.random.seed(42)
    n = 1000

    # Simulate realistic heart disease dataset
    age          = np.random.randint(29, 77, n)
    sex          = np.random.randint(0, 2, n)          # 0=Female, 1=Male
    chest_pain   = np.random.randint(0, 4, n)          # 0-3
    blood_press  = np.random.randint(90, 200, n)
    cholesterol  = np.random.randint(150, 400, n)
    blood_sugar  = np.random.randint(0, 2, n)          # >120mg = 1
    max_hr       = np.random.randint(70, 202, n)
    exercise_ang = np.random.randint(0, 2, n)          # 0=No, 1=Yes

    # Risk formula based on real medical factors
    risk = (
        (age > 55).astype(int) * 2 +
        (sex == 1).astype(int) +
        (chest_pain >= 2).astype(int) * 2 +
        (blood_press > 140).astype(int) +
        (cholesterol > 240).astype(int) +
        blood_sugar +
        (max_hr < 120).astype(int) * 2 +
        exercise_ang * 2 +
        np.random.randint(0, 3, n)
    )
    target = (risk >= 6).astype(int)

    X = np.column_stack([age, sex, chest_pain, blood_press,
                         cholesterol, blood_sugar, max_hr, exercise_ang])
    y = target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"✅ Model trained — Accuracy: {acc*100:.1f}%")

    with open("heart_model.pkl", "wb") as f:
        pickle.dump(model, f)

    return model, round(acc * 100, 1)

# Train on startup if no saved model
if not os.path.exists("heart_model.pkl"):
    model, accuracy = train_model()
else:
    with open("heart_model.pkl", "rb") as f:
        model = pickle.load(f)
    accuracy = "Loaded"

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html", accuracy=accuracy)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            int(request.form["age"]),
            int(request.form["sex"]),
            int(request.form["chest_pain"]),
            int(request.form["blood_pressure"]),
            int(request.form["cholesterol"]),
            int(request.form["blood_sugar"]),
            int(request.form["max_hr"]),
            int(request.form["exercise_angina"]),
        ]

        input_arr = np.array(features).reshape(1, -1)
        prediction = model.predict(input_arr)[0]
        probability = model.predict_proba(input_arr)[0][1] * 100

        result = "High Risk" if prediction == 1 else "Low Risk"
        color  = "danger"   if prediction == 1 else "safe"

        return render_template("result.html",
                               result=result,
                               probability=round(probability, 1),
                               color=color,
                               features=features)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
