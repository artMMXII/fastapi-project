from fastapi import FastAPI, HTTPException, status
from schemas import STaskAdd, STask

app = FastAPI()

tasks = [{"id": 1, "name": "Тест"}, {"id": 2, "name": "Код"}]


@app.post("/tasks", response_model=STask, status_code=status.HTTP_201_CREATED)
async def create_task(task: STaskAdd):
    task_dict = task.model_dump()
    task_id = len(tasks) + 1
    task_dict["id"] = task_id
    tasks.append(task_dict)

    return task_dict


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    # Пытаемся найти задачу (упрощенная логика поиска)
    current_task = None
    for t in tasks:
        if t["id"] == task_id:
            current_task = t
            break

    # Если задача не найдена (переменная осталась None)
    if current_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Задача с ID {task_id} не найдена"
        )

    return current_task

