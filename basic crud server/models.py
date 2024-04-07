from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    name: str
    id: int
    age: int
    classes: List[str]
