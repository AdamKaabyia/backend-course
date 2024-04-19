from fastapi import FastAPI
from app import models
from app.routes import student, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student.router)
app.include_router(auth.router)
