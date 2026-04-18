# ! DOMAIN: Module tính học bổng sinh viên
# NOTE: Input = danh sách sinh viên (mock)
# NOTE: Output = in ra console thông tin + học bổng


class SinhVien:
    # ! ENTITY: Đại diện cho sinh viên trong hệ thống

    def __init__(self, ma_sinh_vien, ten_sinh_vien, diem_trung_binh=0):
        # * INIT FLOW: khởi tạo dữ liệu đầu vào cho object
        self.ma_sinh_vien = ma_sinh_vien
        self.ten_sinh_vien = ten_sinh_vien
        self.diem_trung_binh = diem_trung_binh

    def tinh_hoc_bong(self):
        # * CORE FLOW:
        # 1. Validate dữ liệu
        # 2. Áp dụng rule business
        # 3. Trả về kết quả

        # ? VALIDATION: điểm có hợp lệ không (0 - 10)
        if not (0 <= self.diem_trung_binh <= 10):
            raise ValueError("Điểm trung bình không hợp lệ!")

        # ! BUSINESS RULE: chính sách học bổng (có thể thay đổi theo công ty)
        # TODO: nên đưa rule này ra config / database để dễ maintain

        if self.diem_trung_binh >= 9:
            return 1000000
        elif self.diem_trung_binh >= 8:
            return 500000
        elif self.diem_trung_binh >= 7:
            return 200000
        else:
            return 0


# ! DATA SOURCE: giả lập dữ liệu (thực tế sẽ lấy từ DB/API)
danh_sach_sv = [
    SinhVien("PC06500", "Nguyễn Hồ Vũ", 8),
    SinhVien("PC06400", "Lưu Thanh Nghĩa", 7),
    SinhVien("PC05400", "Lê Minh Khôi", 9),
]


# * MAIN FLOW:
# 1. Duyệt danh sách sinh viên
# 2. Gọi hàm tính học bổng (business logic)
# 3. Format dữ liệu output
# 4. In ra console

for sv in danh_sach_sv:
    # * STEP: gọi logic tính học bổng cho từng sinh viên
    hoc_bong = sv.tinh_hoc_bong()

    # NOTE: format số tiền có dấu phẩy (1,000,000)
    print(
        f"Sinh viên: {sv.ten_sinh_vien} | "
        f"Điểm: {sv.diem_trung_binh} điểm | "
        f"Học bổng nhận được: {hoc_bong:,d} VNĐ"
    )
