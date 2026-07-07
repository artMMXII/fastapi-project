from fastapi import FastAPI, status
from schemas import STaskAdd, STask

app = FastAPI()

tasks = []


@app.post("/tasks", response_model=STask, status_code=status.HTTP_201_CREATED)
async def create_task(task: STaskAdd):
    task_dict = task.model_dump()
    task_id = len(tasks) + 1
    task_dict["id"] = task_id
    tasks.append(task_dict)

    return task_dict