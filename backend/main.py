from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Consumer Health AI Backend Running"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    allowed = [".jpg", ".jpeg", ".png"]

    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in allowed:
        return {"error": "Only JPG and PNG images allowed"}

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "message": "Image uploaded successfully"
    }