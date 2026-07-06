from fastapi import FastAPI
from schemas import STaskAdd, STask

app = FastAPI()

tasks = []


@app.post("/tasks", response_model=STask)
async def create_task(task: STaskAdd):
    # 1. Превращаем Pydantic-модель в словарь
    task_dict = task.model_dump()

    # 2. Генерируем ID (просто берем длину списка + 1)
    # В реальной БД это происходит автоматически
    task_id = len(tasks) + 1
    task_dict["id"] = task_id

    # 3. Сохраняем в список
    tasks.append(task_dict)

    # 4. Возвращаем словарь.
    # FastAPI сам превратит его в схему STask (проверит наличие ID)
    return task_dict