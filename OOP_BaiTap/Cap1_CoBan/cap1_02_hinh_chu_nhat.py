from abc import ABC, abstractmethod


# ! Class trừu tượng: đóng vai trò "hợp đồng" cho tất cả hình học
# * Quy định: mọi hình đều phải có chu_vi() và dien_tich()
class HinhHoc(ABC):

    # * Hàm khởi tạo: chứa dữ liệu chung (hiện tại áp dụng cho hình chữ nhật)
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    # ! Method bắt buộc override: tính chu vi
    # ? Nếu class con không override thì sao? → Không thể khởi tạo object
    @abstractmethod
    def chu_vi(self):
        pass

    # ! Method bắt buộc override: tính diện tích
    @abstractmethod
    def dien_tich(self):
        pass


# * Class con kế thừa từ HinhHoc → phải implement đầy đủ method abstract
class HinhChuNhat(HinhHoc):

    # * Logic tính chu vi hình chữ nhật
    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    # * Logic tính diện tích hình chữ nhật
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong


# * Flow chạy chương trình
# 1. Tạo object HinhChuNhat → gọi __init__ từ class cha
hcn = HinhChuNhat(4, 6)

# 2. Gọi method đã override ở class con
print("Chu vi:", hcn.chu_vi())  # → 2 * (4 + 6) = 20
print("Diện tích:", hcn.dien_tich())  # → 4 * 6 = 24


# NOTE:
# - HinhHoc không thể khởi tạo trực tiếp vì có abstractmethod
# - HinhChuNhat phải override đầy đủ mới dùng được
# - Thiết kế này giúp mở rộng thêm nhiều hình khác mà không sửa code cũ

# TODO:
# - Tạo thêm class HinhVuong, HinhTron
# - Viết chương trình quản lý danh sách nhiều hình (list)
# - Tính tổng diện tích tất cả hình (áp dụng polymorphism)
