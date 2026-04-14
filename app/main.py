from fastapi import FastAPI
from app.config import settings

app = FastAPI(title=settings.app_name)
@app.get("/")
async def root():
    return {"message": "Hello, Async FastAPI!"}