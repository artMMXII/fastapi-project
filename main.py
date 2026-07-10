from fastapi import FastAPI
from routers import tasks_router

app = FastAPI()

app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "Hello!"}
