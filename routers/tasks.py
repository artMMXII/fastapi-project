from fastapi import APIRouter, HTTPException, status
from schemas import STask, STaskAdd


router = APIRouter(prefix="/tasks", tags=["Задачи"])

tasks = []

@router.post("/", response_model=STask, status_code=status.HTTP_201_CREATED)
async def create_task(task: STaskAdd):
    task_dict = task.model_dump()
    task_id = len(tasks) + 1
    task_dict["id"] = task_id
    tasks.append(task_dict)

    return task_dict


@router.get("/")
async def get_tasks():
    return tasks


@router.get("/{task_id}", response_model=STask)
async def get_task(task_id: int):
    # Ищем задачу в списке
    for task in tasks:
        if task["id"] == task_id:
            return task

    # Если дошли до этой строки, значит, return не сработал (задача не найдена)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Задача с ID {task_id} не найдена"
    )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Задача не найдена'
    )
