from pydantic import BaseModel, Field

class STaskAdd(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    priority: int = Field(
        default=1,
        ge=1,
        le=5
    )

    description: str | None = Field(
        default=None,
        max_length=300,
        title="Краткое описание",
        description='Подробное описание задачи'
    )
