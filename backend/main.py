from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from models.predictor import predict_image
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Consumer Health AI Backend Running"}

@app.post("/predict")
async def upload_image(file: UploadFile = File(...)):

    allowed = [".jpg", ".jpeg", ".png"]

    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in allowed:
        return {"error": "Only JPG and PNG images allowed"}

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction, confidence = predict_image(file_path)

    return {
        "filename": file.filename,
        "prediction": prediction,
        "confidence": confidence
    }