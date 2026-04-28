from sinh_vien import Student
from quan_ly_sinh_vien import StudentManager


def main():
    manager = StudentManager()

    # ===== TEST 1: TẠO DỮ LIỆU =====
    print("\n===== TEST 1: TẠO DỮ LIỆU =====")
    s1 = Student("id01", "nguyen van a", 20, 8.5)
    s2 = Student("id02", "tran thi b", 21, 6.8)
    s3 = Student("id03", "le van c", 19, 4.9)
    s4 = Student("id04", "pham van d", 22, 7.2)

    # ===== TEST 2: THÊM =====
    print("\n===== TEST 2: THÊM SINH VIÊN =====")
    for s in [s1, s2, s3, s4]:
        manager.add_student(s)

    # ===== TEST 3: TRÙNG MÃ =====D
    print("\n===== TEST 3: TRÙNG MÃ =====")
    try:
        s_duplicate = Student("id01", "test", 20, 5)
        manager.add_student(s_duplicate)
    except Exception as e:
        print("Lỗi:", e)

    # ===== TEST 4: HIỂN THỊ =====
    print("\n===== TEST 4: DANH SÁCH =====")
    manager.display_the_list_of_students()

    # ===== TEST 5: TÌM =====
    print("\n===== TEST 5: TÌM SINH VIÊN =====")
    result = manager.search_by_id("id02")
    print("Tìm thấy:", result)

    # ===== TEST 6: UPDATE =====
    print("\n===== TEST 6: CẬP NHẬT =====")
    manager.update_student_gpa("id03", 5.5)
    manager.display_the_list_of_students()

    # ===== TEST 7: DELETE =====
    print("\n===== TEST 7: XÓA =====")
    manager.delete_student_by_id("id02")
    manager.display_the_list_of_students()

    # ===== TEST 8: SORT GPA =====
    print("\n===== TEST 8: SORT GPA =====")
    manager.sort_by_gpa()
    manager.display_the_list_of_students()

    # ===== TEST 9: SORT NAME =====
    print("\n===== TEST 9: SORT NAME =====")
    manager.sort_by_name()
    manager.display_the_list_of_students()

    # ===== TEST 10: THỐNG KÊ =====
    print("\n===== TEST 10: THỐNG KÊ =====")
    manager.statistical_data()


if __name__ == "__main__":
    main()
