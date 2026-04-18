# ! DOMAIN: Quản lý phương tiện gồm Xe Máy và Xe Điện
# NOTE: Áp dụng OOP - Inheritance (Kế thừa)
# NOTE: XeDien sẽ dùng lại thuộc tính chung từ XeMay và thêm thuộc tính riêng


class XeMay:
    # ! PARENT CLASS: chứa các thuộc tính chung của mọi xe máy

    def __init__(self, bien_so, hang_xe, gia_ban):
        # * INIT FLOW: khởi tạo thông tin chung
        self.bien_so = bien_so
        self.hang_xe = hang_xe
        self.gia_ban = gia_ban

    def show_info(self):
        # * CORE FLOW: hiển thị thông tin cơ bản
        print("===== THÔNG TIN XE =====")
        print(f"Biển số: {self.bien_so}")
        print(f"Hãng xe: {self.hang_xe}")
        print(f"Giá bán: {self.gia_ban:,d} VNĐ")


class XeDien(XeMay):
    # ! CHILD CLASS: kế thừa từ XeMay
    # NOTE: Có toàn bộ thuộc tính chung + thêm pin riêng

    def __init__(self, bien_so, hang_xe, gia_ban, dung_luong_pin):
        # * STEP 1: gọi class cha để lấy thuộc tính chung
        super().__init__(bien_so, hang_xe, gia_ban)

        # * STEP 2: thêm thuộc tính riêng của xe điện
        self.dung_luong_pin = dung_luong_pin

    def show_info(self):
        # * OVERRIDE FLOW:
        # 1. Dùng lại show_info của cha
        # 2. Bổ sung thông tin riêng

        super().show_info()
        print(f"Dung lượng pin: {self.dung_luong_pin} kWh")


# ! MAIN FLOW:
# 1. Tạo object XeMay
# 2. Tạo object XeDien
# 3. Gọi method hiển thị thông tin

xe_1 = XeMay("65B1-12345", "Honda", 35000000)
xe_2 = XeDien("65M1-67890", "VinFast", 52000000, 3.5)

# * STEP: Hiển thị xe máy thường
xe_1.show_info()

print()

# * STEP: Hiển thị xe điện
xe_2.show_info()
