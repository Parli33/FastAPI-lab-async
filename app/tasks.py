import asyncio
from app.storage import update_task

async def long_running_task(task_id: str, input_data: dict):
    try:
        # Имитация долгой обработки (например, анализ изображения)
        total_steps = 10
        for step in range(1, total_steps + 1):
            await asyncio.sleep(1) # имитация работы
            # обновляем прогресс (дополнительное поле)
            update_task(task_id, "running", {"progress": step, "total": total_steps})
        # Финальный результат
        result = {"output": f"Processed {input_data.get('name', 'unknown task')}"}
        update_task(task_id, "completed", result)
    except Exception as e:
        update_task(task_id, "error", {"error": str(e)})