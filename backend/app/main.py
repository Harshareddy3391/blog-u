from fastapi import FastAPI
from app.database import engine
from app.models.post import Post
from app.models.user import User
from app.models.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello i an harsha"}