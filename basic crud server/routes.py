from fastapi import APIRouter
from typing import List
from models import Student
import db_manager

router = APIRouter()


@router.get("/students/", response_model=List[Student])
def read_students():
    """Get all students."""
    return db_manager.get_all_students()


@router.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    """Get a specific student by ID."""
    return db_manager.get_student(student_id)


@router.post("/students/", response_model=Student)
def create_student(student: Student):
    """Add a new student."""
    db_manager.add_student(student)
    return student


@router.get("/classes/{class_name}/students", response_model=List[Student])
def read_students_in_class(class_name: str):
    """Get all students in a specific class."""
    return db_manager.get_students_in_class(class_name)
