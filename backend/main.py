from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Consumer Health AI Backend Running"}