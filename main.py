from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.joblib")

@app.get("/")
def root():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(data: list):
    prediction = model.predict([data])
    return {"prediction": prediction.tolist()}