import random
from models.student import Student
from services.student_service import StudentService

names = [
    "Nguyen Van A",
    "Tran Thi B",
    "Le Van C",
    "Pham Thi D",
    "Hoang Van E",
    "Vu Thi F",
    "Dang Van G",
    "Bui Thi H",
]


def seed(n=1000):
    service = StudentService()

    for i in range(1, n + 1):
        student_id = f"ID_{i:03d}"
        full_name = random.choice(names)
        age = random.randint(18, 25)
        gpa = round(random.uniform(5, 10), 2)

        try:
            student = Student(student_id, full_name, age, gpa)
            service.add(student)
        except Exception as e:
            print("Lỗi:", e)

    print(f"Đã tạo {n} sinh viên")


if __name__ == "__main__":
    seed(1000)
