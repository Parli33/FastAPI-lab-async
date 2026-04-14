from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.storage import create_task, get_task
from app.tasks import long_running_task

router = APIRouter(prefix="/tasks", tags=["long tasks"])
@router.post("/process")
async def start_processing(input_data: dict, background_tasks: BackgroundTasks):
    task_id = create_task()
    # Запускаем фоновую задачу (не блокирует ответ)
    background_tasks.add_task(long_running_task, task_id, input_data)
    return {"task_id": task_id}
@router.get("/{task_id}")
async def get_task_status(task_id: str):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
"""
router = APIRouter(prefix="/notify", tags=["notifications"])

# симуляция работы SMTP
def send_email(email: str, message: str):
    # Имитация отправки email (синхронная операция)
    import time
    time.sleep(2)
    print(f"Email sent to {email}: {message}")

@router.post("/email")
async def notify_email(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    return {"status": "email will be sent in background"}
"""