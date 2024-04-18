from typing import Optional, List
from sqlmodel import Field, SQLModel, create_engine
from enum import Enum

DB_FILE = "db.sqlite3"
engine = create_engine(f"sqlite:///{DB_FILE}", echo = True)

class Gender(str, Enum):
    male ="male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class UserModel(SQLModel, table = True):
    id : Optional[int] = Field(default= None, primary_key= True)
    first_name : str
    last_name : str
    middle_name : Optional[str] = None
    gender : Gender
    


def create_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()