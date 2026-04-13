# ML Model Deployment with FastAPI and Docker

## Features
- ML model trained using sklearn
- FastAPI for serving predictions
- Docker containerization

## Run Locally
pip install -r requirements.txt
uvicorn main:app --reload

## Run with Docker
docker build -t ml-api .
docker run -p 8000:8000 ml-api

## API Endpoints
- GET / → Check API
- POST /predict → Get prediction

