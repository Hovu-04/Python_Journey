from models.student import Student
from services.student_service import StudentService


def main():
    service = StudentService()

    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Thêm")
        print("2. Xem")
        print("3. Tìm ID")
        print("4. Sửa")
        print("5. Xóa")
        print("6. Tìm tên")
        print("7. Thống kê")
        print("8. Sắp xếp theo GPA")
        print("9. Sắp xếp theo tên")
        print("0. Thoát")

        choice = input("Chọn: ").strip()

        if choice == "1":
            try:
                student = Student(
                    input("ID: "),
                    input("Tên: "),
                    int(input("Tuổi: ")),
                    float(input("GPA: ")),
                )
                service.add(student)
            except Exception as e:
                print("Lỗi:", e)

        elif choice == "2":
            students = service.get_all()
            if not students:
                print("Danh sách trống")
            else:
                for s in students:
                    print(s)

        elif choice == "3":
            s = service.find_by_id(input("ID: "))
            print(s if s else "Không tìm thấy")

        elif choice == "4":
            try:
                student = Student(
                    input("ID cần sửa: "),
                    input("Tên mới: "),
                    int(input("Tuổi mới: ")),
                    float(input("GPA mới: ")),
                )
                service.update(student)
            except Exception as e:
                print("Lỗi:", e)

        elif choice == "5":
            service.delete(input("ID cần xóa: "))

        elif choice == "6":
            result = service.search_by_name(input("Tên: "))
            if result:
                for s in result:
                    print(s)
            else:
                print("Không tìm thấy")

        elif choice == "7":
            service.stats()

        elif choice == "8":
            service.sort_by_gpa()
            print("Đã sắp xếp theo GPA")

        elif choice == "9":
            service.sort_by_name()
            print("Đã sắp xếp theo tên")

        elif choice == "0":
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()
