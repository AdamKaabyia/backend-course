from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    guest = "guest"


class Student(BaseModel):
    name: str
    id: int
    age: int
    classes: List[str]


class User(BaseModel):
    username: str
    password: str  # In practice, store hashes
    role: str  # "admin" or "guest"


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
