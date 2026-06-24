from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="Учебное приложение для курса по FastAPI",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
