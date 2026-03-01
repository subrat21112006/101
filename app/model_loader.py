import pickle
import os

MODEL_PATH = os.path.join("model", "pass_fail_model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found. Run model.py first.")

    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    return model