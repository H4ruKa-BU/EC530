from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict
import uuid

app = FastAPI()

users_db = {}
houses_db = {}
rooms_db = {}
devices_db = {}

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    password: str

@app.post("/users/", response_model=User)
def create_user(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.email] = user
    return user
