# =========================================
# ! XE ĐẠP - MODEL ĐƠN GIẢN (KHÔNG KẾ THỪA)
# =========================================
class XeDap:
    def __init__(self, bien_so, mau_xe, gia_ngay, loai_xe, hang_xe, phi_thue_pin=0):
        # * Thông tin cơ bản
        self.bienso = bien_so
        self.mau_xe = mau_xe
        self.gia_ngay = gia_ngay

        # ! Tách rõ: loại vs hãng
        self.loai_xe = loai_xe  # "thuong" | "dien"
        self.hang_xe = hang_xe  # "Yamaha", "Vinfast"

        # * Trạng thái thuê
        self.co_mua_baohiem = False
        self.ngay_thue = 0

        # * Phí thêm (chỉ dùng cho xe điện)
        self.phi_thue_pin = phi_thue_pin

    # =========================================
    # * TÍNH TIỀN (gom logic lại rõ ràng)
    # =========================================
    def tinh_tong_tien(self):
        tong = self.gia_ngay * self.ngay_thue

        # * Bảo hiểm
        if self.co_mua_baohiem:
            tong += 10000 * self.ngay_thue

        # * Pin (chỉ áp dụng xe điện)
        if self.loai_xe == "dien":
            tong += self.phi_thue_pin * self.ngay_thue

        return tong


# =========================================
# ! TEST
# =========================================
xedap_dien = XeDap(
    bien_so="64-A1111",
    mau_xe="Đỏ",
    gia_ngay=100000,
    loai_xe="dien",  # ✔ đúng
    hang_xe="Yamaha",
    phi_thue_pin=20000,
)

xedap_dien.ngay_thue = 7
xedap_dien.co_mua_baohiem = True

print(f"Tổng tiền phải trả: {xedap_dien.tinh_tong_tien():,.0f} VND")
