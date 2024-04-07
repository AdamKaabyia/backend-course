import json
from typing import List
from models import Student

DATABASE_FILE = 'students_db.json'


def read_db() -> List[Student]:
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def write_db(data: List[Student]):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(data, file, default=lambda o: o.__dict__)


def get_all_students() -> List[Student]:
    return read_db()


def get_student(student_id: int) -> Student:
    students = read_db()
    for student in students:
        if student['id'] == student_id:
            return student
    return None


def add_student(student: Student):
    students = read_db()
    students.append(student)
    write_db(students)


def get_students_in_class(class_name: str) -> List[Student]:
    students = read_db()
    return [student for student in students if class_name in student['classes']]
