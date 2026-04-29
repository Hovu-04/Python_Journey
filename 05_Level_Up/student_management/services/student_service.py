from repository.student_repository import StudentRepository
from utils.logger import log


class StudentService:
    def __init__(self):
        self.repo = StudentRepository()
        self.students = self.repo.load()

    def auto_save(self):
        self.repo.save(self.students)

    def add(self, student):
        if any(s.student_id == student.student_id for s in self.students):
            log(f"ADD FAIL - Trùng mã: {student.student_id}")
            return

        self.students.append(student)
        self.auto_save()
        log(f"ADD SUCCESS - {student.student_id} - {student.full_name}")

    def get_all(self):
        return self.students

    def find_by_id(self, student_id):
        student_id = student_id.strip().upper()

        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def update(self, student):
        old = self.find_by_id(student.student_id)

        if not old:
            log(f"UPDATE FAIL - Không tìm thấy: {student.student_id}")
            return False

        old.full_name = student.full_name
        old.age = student.age
        old.gpa = student.gpa

        self.auto_save()
        log(f"UPDATE SUCCESS - {student.student_id} - {student.full_name}")
        return True

    def delete(self, student_id):
        student = self.find_by_id(student_id)
        if not student:
            log(f"DELETE FAIL - Không tìm thấy: {student_id}")
            return False

        confirm = (
            input(f"Bạn có chắc muốn xóa {student.full_name}? (y/n): ").strip().lower()
        )
        if confirm != "y":
            log(f"DELETE CANCEL - {student_id}")
            return False

        self.students.remove(student)
        self.auto_save()
        log(f"DELETE SUCCESS - {student_id}")
        return True

    def sort_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)
        log("SORT SUCCESS - Theo GPA giảm dần")

    def sort_by_name(self):
        self.students.sort(key=lambda s: s.full_name)
        log("SORT SUCCESS - Theo tên A-Z")

    def stats(self):
        if not self.students:
            print("Danh sách trống!")
            return
        avg = sum(s.gpa for s in self.students) / len(self.students)
        print(f"GPA trung bình: {round(avg,2)}")
