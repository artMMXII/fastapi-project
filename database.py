from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

# 1. Настройка URL для SQLite (асинхронный драйвер aiosqlite)
DATABASE_URL = "sqlite+aiosqlite:///tasks.db"

# 2. Создание движка (Engine)
engine = create_async_engine(DATABASE_URL)

# 3. Фабрика сессий (Session Factory)
new_session = async_sessionmaker(engine, expire_on_commit=False)

# 4. Базовый класс моделей
class Model(MappedAsDataclass, DeclarativeBase):
    pass
