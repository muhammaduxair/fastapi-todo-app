from fastapi import FastAPI
from todo_router import router as todo_router

app = FastAPI()

app.include_router(todo_router)
