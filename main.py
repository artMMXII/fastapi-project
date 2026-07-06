from fastapi import FastAPI
from schemas import STaskAdd

app = FastAPI()

# Имитация базы данных
tasks = []

@app.get("/tasks")
async def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
async def add_task(task: STaskAdd):
    # 1. Добавляем задачу в список.
    # Чтобы сохранить её как словарь, используем model_dump()
    tasks.append(task.model_dump())

    # 2. Очищаем список (для теста)
    # Если список стал слишком большим, удаляем старые (опционально)
    if len(tasks) > 20:
        tasks.clear()

    # 3. Возвращаем подтверждение
    return {"ok": True, "message": "Задача добавлена"}