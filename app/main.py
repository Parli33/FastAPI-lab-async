from contextlib import asynccontextmanager
import asyncio
from fastapi import FastAPI
from app.config import settings
from app.routers import tasks_router, websocket_router
from app.tasks import task_worker

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(task_worker())
    yield

app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(tasks_router)
app.include_router(websocket_router)
@app.get("/")
async def root():
    return {"message": "Hello, Async FastAPI!"}