from fastapi import FastAPI
from routes import router as student_router

app = FastAPI()

app.include_router(student_router)
