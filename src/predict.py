from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/predict/{name}")
def predict_name(name: str):
    # Apply the same preprocessing as training!
    length = len(name.lower().strip())
    prediction = model.predict([[length]])
    return {"name": name, "prediction": int(prediction[0])}