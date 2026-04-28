class StudentManager:
    def __init__(self):
        self.list_student = []

    def search_by_id(self, student_id):  # sourcery skip: use-next
        student_id = student_id.strip().upper()

        for student in self.list_student:
            if student.student_id == student_id:
                return student
        return None

    def add_student(self, student_object):
        if self.search_by_id(student_id=student_object.student_id):
            print("Mã sinh viên đã tồn tại!")
            return
        self.list_student.append(student_object)
        print("Thêm sinh viên thành công!")

    def display_the_list_of_students(self):
        if not self.list_student:
            print("Danh sách sinh viên đang trống!")
            return
        for student in self.list_student:
            print(student)

    def update_student_gpa(self, student_id, new_gpa):
        student = self.search_by_id(student_id)

        if not student:
            print("Không tìm thấy sinh viên")
            return

        try:
            student.gpa = new_gpa
            print("Cập nhật điểm trung bình thành công!")
        except ValueError as e:
            print("Lỗi:", e)

    def delete_student_by_id(self, student_id):
        # sourcery skip: use-named-expression
        student = self.search_by_id(student_id=student_id)
        if student:
            self.list_student.remove(student)
            print("Xóa sinh viên thành công!")
        else:
            print("Không tìm thấy sinh viên")

    def sort_by_gpa(self):
        n = len(self.list_student)

        for i in range(n):
            for j in range(i + 1, n):
                if self.list_student[i].gpa < self.list_student[j].gpa:
                    temp = self.list_student[i]
                    self.list_student[i] = self.list_student[j]
                    self.list_student[j] = temp
        print("Đã sắp xếp theo điểm giảm dần!")

    def sort_by_name(self):
        n = len(self.list_student)

        for i in range(n):
            for j in range(i + 1, n):
                if self.list_student[i].full_name > self.list_student[j].full_name:
                    temp = self.list_student[i]
                    self.list_student[i] = self.list_student[j]
                    self.list_student[j] = temp
        print("Đã sắp xếp theo tên!")

    def statistical_data(self):
        # sourcery skip: convert-to-enumerate, move-assign-in-block, remove-unused-enumerate
        if len(self.list_student) == 0:
            print("Chưa có dữ liệu thống kê!")
            return

        sum_student = 0
        sum_gpa = 0

        good = 0
        rather = 0
        medium = 0
        weak = 0

        highest_scoring_student = self.list_student[0]

        for student in self.list_student:
            sum_student += 1
            sum_gpa += student.gpa

            # tìm sinh viên điểm cao nhất
            if student.gpa > highest_scoring_student.gpa:
                highest_scoring_student = student

            rating = student.rating

            if rating == "Giỏi":
                good += 1
            elif rating == "Khá":
                rather += 1
            elif rating == "Trung bình":
                medium += 1
            elif rating == "Yếu":
                weak += 1

        class_average_score = sum_gpa / sum_student
        print("===== THỐNG KÊ =====")
        print("Tổng sinh viên:", sum_student)
        print("Điểm trung bình lớp:", round(class_average_score, 2))
        print("Sinh viên điểm cao nhất:", highest_scoring_student.full_name)

        print("Giỏi:", good)
        print("Khá:", rather)
        print("Trung bình:", medium)
        print("Yếu:", weak)
