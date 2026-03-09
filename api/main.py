from fastapi import FastAPI
from predictor import predict_match

app = FastAPI()

@app.post("/predict")
def predict(features: dict):
    return predict_match(features)

# Run: uvicorn api.main:app --reload