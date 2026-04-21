# ! DOMAIN: Quản lý nhân viên với dữ liệu nhạy cảm (lương)


class NhanVien:
    # ! ENTITY: Nhân viên (có thông tin cơ bản + lương riêng tư)

    def __init__(self, ma_nv, ten_nv, luong_nv):
        # * INIT FLOW: khởi tạo dữ liệu
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv

        # ! ENCAPSULATION: thuộc tính private (không truy cập trực tiếp)
        self.__luong_nv = luong_nv

    # * GETTER: cho phép đọc lương thông qua method
    def get_luong(self):
        # NOTE: có thể thêm logic kiểm tra quyền tại đây
        return self.__luong_nv

    # * SETTER: cho phép cập nhật lương có kiểm soát
    def set_luong(self, luong_moi):
        # ? VALIDATION: lương phải >= 0
        if luong_moi < 0:
            raise ValueError("Lương không hợp lệ!")

        # * STEP: cập nhật lương
        self.__luong_nv = luong_moi

    def show_info(self):
        # * CORE FLOW:
        # 1. Lấy dữ liệu
        # 2. Hiển thị thông tin (không expose trực tiếp biến private)

        print("==============================")
        print(f"Mã nhân viên: {self.ma_nv}")
        print(f"Tên nhân viên: {self.ten_nv}")

        # NOTE: truy cập lương thông qua getter (đúng chuẩn đóng gói)
        print(f"Lương: {self.get_luong():,d} VNĐ")


# ! MAIN FLOW:
# 1. Tạo nhân viên
# 2. Không truy cập trực tiếp __luong_nv
# 3. Sử dụng getter/setter để thao tác

nv = NhanVien("NV001", "Nguyễn Hồ Vũ", 500000)

# * STEP: hiển thị thông tin ban đầu
nv.show_info()

# * STEP: cập nhật lương qua setter
nv.set_luong(800000)

# * STEP: hiển thị lại sau khi cập nhật
nv.show_info()

# ? TEST: nếu truy cập trực tiếp sẽ lỗi (đúng yêu cầu bài)
# print(nv.__luong_nv)  # ❌ AttributeError
