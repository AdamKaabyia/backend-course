import json
from typing import List
from models import Student, User, UserInDB


def read_db(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def write_db(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


# Example functions for students
def get_all_students():
    students = read_db('students_db.json')
    return students


# Add similar CRUD functions for students

# Example functions for users
def get_user_by_username(username: str):
    users = read_db('users_db.json')
    user = next((user for user in users if user['username'] == username), None)
    return user


def add_user(user: UserInDB):
    users = read_db('users_db.json')
    users.append(user.dict())
    write_db(users, 'users_db.json')
