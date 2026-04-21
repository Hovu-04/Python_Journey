from abc import ABC, abstractmethod


# =========================================
# ! ABSTRACT BASE CLASS
# Khung chung cho mọi loại phương tiện thuê
# =========================================
class PhuongTienThue(ABC):
    def __init__(self, bien_so, gia_co_ban_ngay, so_ngay_thue):
        """
        FLOW KHỞI TẠO:
        1. Nhận thông tin xe + giá + số ngày thuê
        2. Validate dữ liệu đầu vào
        3. Lưu trạng thái vào object
        """

        # * STEP 1: Validate input
        if gia_co_ban_ngay <= 0:
            raise ValueError("Giá phải > 0")
        if so_ngay_thue <= 0:
            raise ValueError("Số ngày phải > 0")

        # * STEP 2: Lưu dữ liệu
        self.bien_so = bien_so
        self.gia_co_ban_ngay = gia_co_ban_ngay
        self.so_ngay_thue = so_ngay_thue

    # =========================================
    # ! ABSTRACT METHOD (HOOK)
    # =========================================
    @abstractmethod
    def tinh_chi_phi_phu(self):
        """
        CONTRACT:
        - Mỗi loại xe phải tự định nghĩa chi phí phụ
        - Được gọi bên trong tinh_tong_tien()
        """
        pass

    # =========================================
    # ! TEMPLATE METHOD (CORE FLOW)
    # =========================================
    def tinh_tong_tien(self):
        """
        FLOW TÍNH TIỀN:
        1. Tính tiền thuê cơ bản (giá * ngày)
        2. Gọi method của class con để lấy chi phí phụ
        3. Cộng lại thành tổng tiền

        → Đây là Template Method Pattern
        → Class cha giữ flow, class con cung cấp chi tiết
        """

        # * STEP 3: Tiền cơ bản
        tien_co_ban = self.gia_co_ban_ngay * self.so_ngay_thue

        # * STEP 4: Chi phí phụ (polymorphism xảy ra tại đây)
        chi_phi_phu = self.tinh_chi_phi_phu()

        # * STEP 5: Tổng hợp
        return tien_co_ban + chi_phi_phu


# =========================================
# ? XE ĐẠP THƯỜNG
# =========================================
class XeDapThuong(PhuongTienThue):
    def tinh_chi_phi_phu(self):
        # FLOW: phí cố định → không phụ thuộc ngày
        return 5000


# =========================================
# ? XE ĐẠP ĐIỆN
# =========================================
class XeDapDien(PhuongTienThue):
    def tinh_chi_phi_phu(self):
        # FLOW: phí pin → phụ thuộc số ngày thuê
        return 20000 * self.so_ngay_thue


# =========================================
# ? XE ĐẠP ĐÔI
# =========================================
class XeDapDoi(PhuongTienThue):
    def tinh_chi_phi_phu(self):
        # FLOW: phí bảo trì cao → theo ngày
        return 15000 * self.so_ngay_thue


# =========================================
# ! MAIN FLOW (ENTRY POINT)
# =========================================
if __name__ == "__main__":

    """
    FLOW CHƯƠNG TRÌNH:

    STEP A: Tạo danh sách các loại xe (đa hình - polymorphism)
    STEP B: Lặp qua từng xe
    STEP C: Gọi cùng 1 method tinh_tong_tien()
    STEP D: Mỗi object tự xử lý logic riêng (dynamic dispatch)
    """

    danh_sach_xe = [
        XeDapThuong("29-A1111", 30000, 3),
        XeDapDien("29-B2222", 50000, 3),
        XeDapDoi("29-C3333", 60000, 2),
    ]

    for xe in danh_sach_xe:
        # * STEP D: Polymorphism xảy ra tại đây
        print(f"Xe {xe.bien_so} - Tổng tiền thuê: {xe.tinh_tong_tien():,d}đ")
