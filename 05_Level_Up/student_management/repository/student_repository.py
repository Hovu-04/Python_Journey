import os
import json
from models.student import Student

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "student.json")


class StudentRepository:
    def __init__(self):
        if not os.path.exists(os.path.dirname(FILE_PATH)):
            os.makedirs(os.path.dirname(FILE_PATH))

        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load(self):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        students = []
        for item in data:
            try:
                students.append(Student(**item))
            except ValueError as e:
                print("Bỏ qua dữ liệu lỗi:", e)
        return students

    def save(self, students):
        data = [sv.to_dict() for sv in students]

        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
