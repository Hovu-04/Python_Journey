# ! DOMAIN: Hệ thống quản lý sách
# NOTE: Chức năng chính:
# NOTE: 1. Thêm sách
# NOTE: 2. Tìm sách theo mã
# NOTE: 3. Cập nhật sách
# NOTE: 4. Xóa sách
# NOTE: 5. Hiển thị danh sách sách


class Sach:
    # ! ENTITY: Đại diện cho một quyển sách

    def __init__(self, ma_sach, ten_sach, gia_ban, so_luong):
        # * INIT FLOW: khởi tạo dữ liệu cho sách
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.gia_ban = gia_ban
        self.so_luong = so_luong

    def hien_thi_thong_tin(self):
        # * OUTPUT FLOW: hiển thị thông tin của 1 sách
        print("===== THÔNG TIN SÁCH =====")
        print(f"Mã sách   : {self.ma_sach}")
        print(f"Tên sách  : {self.ten_sach}")
        print(f"Giá bán   : {self.gia_ban:,d} VND")
        print(f"Số lượng  : {self.so_luong}")
        print("==========================")


class QuanLySach:
    # ! MANAGER: quản lý danh sách sách

    def __init__(self):
        # * INIT FLOW: tạo danh sách rỗng
        self.danh_sach_sach = []

    def kiem_tra_du_lieu_hop_le(self, ma_sach, ten_sach, gia_ban, so_luong):
        # * VALIDATION FLOW:
        # 1. Kiểm tra dữ liệu bắt buộc
        # 2. Kiểm tra giá bán và số lượng hợp lệ
        # 3. Trả về True nếu hợp lệ, False nếu không hợp lệ

        # ? VALIDATION: mã sách và tên sách không được rỗng
        if not ma_sach or not ten_sach:
            print("Lỗi: Mã sách và tên sách không được để trống!")
            return False

        # ? VALIDATION: giá bán phải > 0
        if gia_ban <= 0:
            print("Lỗi: Giá bán phải lớn hơn 0!")
            return False

        # ? VALIDATION: số lượng phải > 0
        if so_luong <= 0:
            print("Lỗi: Số lượng phải lớn hơn 0!")
            return False

        return True

    def tim_sach_theo_ma(self, ma_sach):
        # * SEARCH FLOW:
        # 1. Duyệt danh sách sách
        # 2. So sánh mã sách
        # 3. Trả về object nếu tìm thấy, ngược lại trả về None

        for sach in self.danh_sach_sach:
            if sach.ma_sach == ma_sach:
                return sach
        return None

    def them_sach(self, ma_sach, ten_sach, gia_ban, so_luong):
        # * CREATE FLOW:
        # 1. Validate dữ liệu đầu vào
        # 2. Kiểm tra trùng mã sách
        # 3. Tạo sách mới
        # 4. Thêm vào danh sách

        if not self.kiem_tra_du_lieu_hop_le(ma_sach, ten_sach, gia_ban, so_luong):
            return

        # ? VALIDATION: không cho trùng mã sách
        if self.tim_sach_theo_ma(ma_sach) is not None:
            print(f"Lỗi: Mã sách '{ma_sach}' đã tồn tại!")
            return

        sach_moi = Sach(ma_sach, ten_sach, gia_ban, so_luong)
        self.danh_sach_sach.append(sach_moi)

        print(f"Thêm sách '{ten_sach}' thành công!")

    def cap_nhat_sach(self, ma_sach, ten_sach_moi, gia_ban_moi, so_luong_moi):
        # * UPDATE FLOW:
        # 1. Tìm sách theo mã
        # 2. Kiểm tra sách có tồn tại không
        # 3. Validate dữ liệu mới
        # 4. Cập nhật thông tin

        sach_can_cap_nhat = self.tim_sach_theo_ma(ma_sach)
        if sach_can_cap_nhat is None:
            print(f"Lỗi: Không tìm thấy sách có mã '{ma_sach}'!")
            return

        if not self.kiem_tra_du_lieu_hop_le(
            ma_sach, ten_sach_moi, gia_ban_moi, so_luong_moi
        ):
            return

        # * STEP: cập nhật dữ liệu
        sach_can_cap_nhat.ten_sach = ten_sach_moi
        sach_can_cap_nhat.gia_ban = gia_ban_moi
        sach_can_cap_nhat.so_luong = so_luong_moi

        print(f"Cập nhật sách có mã '{ma_sach}' thành công!")

    def xoa_sach(self, ma_sach):
        # * DELETE FLOW:
        # 1. Tìm sách theo mã
        # 2. Nếu tồn tại thì xóa
        # 3. Nếu không tồn tại thì báo lỗi

        sach_can_xoa = self.tim_sach_theo_ma(ma_sach)
        if sach_can_xoa is None:
            print(f"Lỗi: Không tìm thấy sách có mã '{ma_sach}' để xóa!")
            return

        self.danh_sach_sach.remove(sach_can_xoa)
        print(f"Đã xóa sách '{sach_can_xoa.ten_sach}' thành công!")

    def hien_thi_tat_ca_sach(self):
        # * OUTPUT FLOW:
        # 1. Kiểm tra danh sách có rỗng không
        # 2. Nếu không rỗng thì hiển thị từng sách

        if not self.danh_sach_sach:
            print("Danh sách sách đang trống!")
            return

        for sach in self.danh_sach_sach:
            sach.hien_thi_thong_tin()


# ! MAIN FLOW:
# 1. Khởi tạo bộ quản lý sách
# 2. Thêm dữ liệu mẫu
# 3. Cập nhật / xóa thử
# 4. Hiển thị danh sách cuối cùng

quan_ly_sach = QuanLySach()

# * STEP: thêm sách
quan_ly_sach.them_sach("BK_01", "Nuốt ngược nước mắt để trưởng thành", 100000, 1000)
quan_ly_sach.them_sach("BK_02", "Thay đổi nhỏ thành công lớn", 80000, 90)
quan_ly_sach.them_sach("BK_03", "Thói quen kỷ luật bản thân", 50000, 20)
quan_ly_sach.them_sach("BK_04", "Học lập trình căn bản với Python", 50000, 20)

# * STEP: cập nhật sách
quan_ly_sach.cap_nhat_sach("BK_03", "Thói quen kỷ luật bản thân", 60000, 25)

# * STEP: xóa sách
quan_ly_sach.xoa_sach("BK_02")

# * STEP: hiển thị danh sách còn lại
quan_ly_sach.hien_thi_tat_ca_sach()
