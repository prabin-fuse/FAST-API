from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Department(str, Enum):
    machine_learning= "machine_learning"
    fullstack = "fullstack"
    finance = "finance"
    hr = "HR"
    logistics = "logistics"


class Employee(BaseModel):
    id: Optional[UUID] = uuid4()
    name : str
    department : Department
    