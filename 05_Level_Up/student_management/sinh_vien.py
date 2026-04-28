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
        if not Student.is_valid_student_id(value):
            raise ValueError(
                "Mã sinh viên phải bắt đầu bằng ID và không được bỏ trống!"
            )

        self._student_id = value.strip().upper()

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Tên sinh viên không được bỏ trống!")
        self._full_name = value.strip().title()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 16:
            raise ValueError("Tuổi sinh viên phải từ 16 trở lên")
        self._age = value

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, (float, int)) or not (0 <= value <= 10):
            raise ValueError("Điểm trung bình phải từ 0 đến 10")
        self._gpa = float(value)

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
        return f"{self.student_id} | {self.full_name} | {self.age} | {self.gpa} | {self.rating}"

    @staticmethod
    def is_valid_student_id(student_ids):
        return isinstance(student_ids, str) and student_ids.strip().upper().startswith(
            "ID"
        )

    @classmethod
    def create_default(cls):
        return cls("ID_001", "Nguyễn Hồ Vũ", 22, 6)
