from pydantic import BaseModel

class StudentInput(BaseModel):
    Study_Hours_per_Week: float
    Attendance_Rate: float
    Past_Exam_Scores: float
    Parental_Education_Level: int
    Internet_Access_at_Home: int
    Extracurricular_Activities: int

class PredictionOutput(BaseModel):
    result: str