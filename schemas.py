from pydantic import BaseModel

# Схема для добавления задачи (то, что присылает пользователь)
class STaskAdd(BaseModel):
    name: str
    description: str | None = None

# Схема для чтения (то, что мы отдаем пользователю)
# Здесь появляется поле id
class STask(BaseModel):
    id: int
    name: str
    description: str | None = None