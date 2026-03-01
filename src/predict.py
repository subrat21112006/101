import pickle
import pandas as pd

# Load trained model
with open("model/pass_fail_model.pkl", "rb") as f:
    model = pickle.load(f)

# Feature order (MUST match training)
columns = [
    "Study_Hours_per_Week",
    "Attendance_Rate",
    "Past_Exam_Scores",
    "Parental_Education_Level",
    "Internet_Access_at_Home",
    "Extracurricular_Activities",
    "Final_Exam_Score"
]

# Take user input
study_hours = float(input("Enter Study Hours per Week: "))
attendance = float(input("Enter Attendance Rate (%): "))
past_score = float(input("Enter Past Exam Score: "))
parent_edu = int(input("Enter Parental Education Level (0/1/2/3): "))
internet = int(input("Internet Access at Home? (1=Yes, 0=No): "))
extra = int(input("Extracurricular Activities? (1=Yes, 0=No): "))
final_score = float(input("Enter Final Exam Score: "))

# Create DataFrame (fix sklearn feature-name error)
user_df = pd.DataFrame([[
    study_hours,
    attendance,
    past_score,
    parent_edu,
    internet,
    extra,
    final_score
]], columns=columns)

# Predict
prediction = model.predict(user_df)

print("\nFinal Result:", "Pass" if prediction[0] == 1 else "Fail")