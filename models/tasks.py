from sqlalchemy.orm import Mapped, mapped_column
from database import Model


class TaskModel(Model):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None] = mapped_column(default=None)
    is_completed: Mapped[bool] = mapped_column(default=False)

