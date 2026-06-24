from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task Manager API",
    description="Учебное приложение для курса по FastAPI",
    version="1.0.0"
)

class User(BaseModel):
    id: int
    name: str
    age: int


users_db = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30},
]

@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}

@app.get("/users")
def get_all_users():
    """Возвращает список всех пользователей"""
    return users_db

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Возвращает конкретного пользователя по ID"""
    for user in users_db:
        if user["id"] == user_id:
            return user
    # Если не нашли — выдаем ошибку 404
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: User):
    """Добавляет нового пользователя"""
    # Превращаем модель Pydantic в словарь и добавляем в список
    users_db.append(user.model_dump())
    return {"message": "User created", "user": user}


@app.put("/users/{user_id}")
def update_user_complete(user_id: int, updated_user: User):
    """Полностью заменяет пользователя с указанным ID"""
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            # Полная замена элемента списка
            users_db[index] = updated_user.model_dump()
            return {"message": "User updated completely", "user": updated_user}

    raise HTTPException(status_code=404, detail="User not found")


# Модель для обновления (все поля могут быть пустыми)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


@app.patch("/users/{user_id}")
def update_user_partial(user_id: int, user_update: UserUpdate):
    """Обновляет только переданные поля"""
    for user in users_db:
        if user["id"] == user_id:
            # Если прислали имя — обновляем имя
            if user_update.name is not None:
                user["name"] = user_update.name
            # Если прислали возраст — обновляем возраст
            if user_update.age is not None:
                user["age"] = user_update.age
            return {"message": "User updated partially", "user": user}

    raise HTTPException(status_code=404, detail="User not found")

