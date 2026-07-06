from fastapi import FastAPI
from schemas import STaskAdd, STask

app = FastAPI()


@app.post("/tasks")
async def create_task(task: STaskAdd) -> STask:
    # Представим, что мы сохранили задачу в БД и получили ID = 1
    # Мы формируем полный словарь данных
    task_dict = task.model_dump()
    task_dict["id"] = 1  # Добавляем ID, которого не было в запросе

    # Допустим, у нас тут есть лишнее секретное поле
    task_dict["secret_code"] = "12345"

    # Возвращаем словарь, в котором ЕСТЬ secret_code
    return task_dict

