import joblib
import numpy as np
import os

MODEL_PATH = os.path.join("model", "pass_fail_model.pkl")

model = joblib.load(MODEL_PATH)

def predict_pass_fail(data: dict) -> str:
    features = np.array([[
        data["Study_Hours_per_Week"],
        data["Attendance_Rate"],
        data["Past_Exam_Scores"],
        data["Parental_Education_Level"],
        data["Internet_Access_at_Home"],
        data["Extracurricular_Activities"]
    ]])

    pred = model.predict(features)[0]
    return "Pass" if pred == 1 else "Fail"