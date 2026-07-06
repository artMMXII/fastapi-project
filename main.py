from fastapi import FastAPI
from schemas import STaskAdd  # Импортируем нашу схему

app = FastAPI()

# Создаем эндпоинт для добавления задачи
@app.post("/tasks")
async def add_task(task: STaskAdd):
    return {"message": "Задача получена", "data": task}

