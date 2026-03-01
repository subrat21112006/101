from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import StudentInput, PredictionOutput
from app.predict import predict_pass_fail

app = FastAPI()

# CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: StudentInput):
    result = predict_pass_fail(data.dict())
    return {"result": result}