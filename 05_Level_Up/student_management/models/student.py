import re


class Student:
    def __init__(self, student_id: str, full_name: str, age: int, gpa: float):
        self.student_id = student_id
        self.full_name = full_name
        self.age = age
        self.gpa = gpa

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not Student.validate_code(value):
            raise ValueError("Mã sinh viên không đúng định dạng")
        self._student_id = value.strip().upper()

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Tên sinh viên không được rỗng!")
        self._full_name = value.strip().title()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 16:
            raise ValueError("Tuổi phải >= 16")
        self._age = value

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, (float, int)) or not (0 <= value <= 10):
            raise ValueError("Điểm phải từ 0 đến 10!")
        self._gpa = float(value)

    @staticmethod
    def validate_code(student_id):
        if not isinstance(student_id, str):
            return False
        return bool(re.match(r"^ID_\d{3}$", student_id.strip().upper()))

    @property
    def rating(self):
        if self.gpa >= 8:
            return "Giỏi"
        elif self.gpa >= 6.5:
            return "Khá"
        elif self.gpa >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"{self.student_id} | {self.full_name} | {self.age} | {self.gpa:.2f} | {self.rating}"

    # Convert Object -> Dictionary(Json)
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "age": self.age,
            "gpa": self.gpa,
        }
