# ! DOMAIN: Hệ thống quản lý cửa hàng bán sách
# NOTE: Gồm 2 class chính:
# NOTE: 1. Sach   -> quản lý sản phẩm / tồn kho
# NOTE: 2. HoaDon -> xử lý mua hàng + tính tiền


class Sach:
    # ! ENTITY: Đại diện cho một cuốn sách trong cửa hàng

    def __init__(self, ma_sach, ten_sach, gia_ban, so_luong):
        # * INIT FLOW: khởi tạo dữ liệu sách
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.gia_ban = gia_ban
        self.so_luong = so_luong

    def show_info(self):
        # * OUTPUT FLOW: hiển thị thông tin sách hiện tại
        print(
            f"[{self.ma_sach}] {self.ten_sach} - "
            f"Giá: {self.gia_ban:,d} VNĐ - "
            f"Số lượng: {self.so_luong}"
        )


class HoaDon:
    # ! ENTITY: Hóa đơn mua hàng của khách

    def __init__(self, ma_hd, ten_khach):
        # * INIT FLOW: tạo thông tin hóa đơn
        self.ma_hd = ma_hd
        self.ten_khach = ten_khach

        # NOTE: list chứa [sach, so_luong_mua]
        self.danh_sach = []

    def them_sach(self, sach, so_luong_mua):
        # * CORE FLOW:
        # 1. Kiểm tra tồn kho
        # 2. Thêm sách vào hóa đơn
        # 3. Trừ tồn kho

        # ? VALIDATION: số lượng mua có hợp lệ không
        if so_luong_mua <= 0:
            print("Số lượng mua phải lớn hơn 0")
            return

        # ? VALIDATION: đủ hàng trong kho không
        if so_luong_mua > sach.so_luong:
            print(f"Không đủ hàng! Kho còn {sach.so_luong} quyển")
            return

        # * STEP: thêm sản phẩm vào giỏ hàng
        self.danh_sach.append([sach, so_luong_mua])

        # * STEP: cập nhật tồn kho sau bán
        sach.so_luong -= so_luong_mua

        print(f"Đã thêm: {sach.ten_sach} x{so_luong_mua}")

    def tinh_tong_tien(self):
        # * BUSINESS LOGIC:
        # duyệt toàn bộ sản phẩm trong hóa đơn
        # cộng thành tiền từng dòng

        tong = 0

        for sach, so_luong_mua in self.danh_sach:
            tong += sach.gia_ban * so_luong_mua

        return tong

    def show_hoa_don(self):
        # * OUTPUT FLOW:
        # 1. In header hóa đơn
        # 2. In từng dòng sản phẩm
        # 3. In tổng tiền

        print("==== HÓA ĐƠN ====")
        print(f"Mã HD    : {self.ma_hd}")
        print(f"Khách    : {self.ten_khach}")
        print("------------------")

        for sach, so_luong_mua in self.danh_sach:
            thanh_tien = sach.gia_ban * so_luong_mua

            print(f"{sach.ten_sach} x{so_luong_mua} = {thanh_tien:,d} VNĐ")

        print("------------------")
        print(f"Tổng tiền: {self.tinh_tong_tien():,d} VNĐ")


# ! MAIN FLOW:
# 1. Tạo dữ liệu sách
# 2. Tạo hóa đơn khách hàng
# 3. Thêm sách vào hóa đơn
# 4. In kết quả cuối cùng

s1 = Sach("S001", "Lập Trình Python", 85000, 10)
s2 = Sach("S002", "Clean Code", 120000, 5)
s3 = Sach("S003", "Đắc Nhân Tâm", 75000, 8)

hd = HoaDon("HD001", "Nguyễn Văn An")

# * STEP: khách chọn sản phẩm
hd.them_sach(s1, 2)
hd.them_sach(s2, 1)
hd.them_sach(s3, 3)

# * STEP: xuất hóa đơn
hd.show_hoa_don()
