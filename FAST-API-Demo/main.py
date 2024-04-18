from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID, uuid4
from sqlmodel import Session, select

from models import User, Gender, Role
from database import UserModel, engine



app = FastAPI()

db: List[User] =[
    User(id = uuid4(), first_name="Prabin", last_name="Bohara", gender= Gender.male, roles= [Role.admin]),
    User(id = uuid4(), first_name="Raju", last_name="Paudel", gender= Gender.male, roles= [Role.user, Role.student])
]




@app.get("/")
def read_root():
    return {"Hello": "prabin"}

@app.get("/api/v1/users")
def fetch_users():
    return db

@app.post("/api/v1/users")
def register_user(user : User):
    db.append(user)
    return {"id" : user.id}

@app.delete("/api/v1/users/{user_id}") # user_id is path variable:
def delete_user(user_id : UUID) :
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    
    raise HTTPException(
        status_code= 404,
        detail = f"user with id: {user_id} does not exists"
    )