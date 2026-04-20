from abc import ABC, abstractmethod


class NhanVien(ABC):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.luong_co_ban = luong_co_ban
        self.phong_ban = phong_ban

    @abstractmethod
    def tinh_luong(self):
        pass

    def hien_thi_thong_tin(self):
        print("===== THÔNG TIN NHÂN VIÊN =====")
        print(f"Mã NV      : {self.ma_nv}")
        print(f"Họ tên     : {self.ten_nv}")
        print(f"Phòng ban  : {self.phong_ban}")
        print(f"Lương CB   : {self.luong_co_ban:,} VND")
        print(f"Thực lãnh  : {self.tinh_luong():,} VND")
        print("===============================")


class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban, phu_cap):
        super().__init__(ma_nv, ten_nv, luong_co_ban, phong_ban)
        self.phu_cap = phu_cap

    def tinh_luong(self):
        return self.luong_co_ban + self.phu_cap


class NhanVienKySu(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban, du_an):
        super().__init__(ma_nv, ten_nv, luong_co_ban, phong_ban)
        self.du_an = du_an

    def tinh_luong(self):
        return self.luong_co_ban + self.du_an


class NhanvienBanHang(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban, doanh_so, hoa_hong):
        super().__init__(ma_nv, ten_nv, luong_co_ban, phong_ban)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    def tinh_luong(self):
        return self.luong_co_ban + self.doanh_so * (self.hoa_hong / 100)


class QuanLyNhanVien:
    def __init__(self):
        self.list_nhan_vien = []

    def nhap_thong_tin_chung(self):
        thong_tin = {
            "ma_nv": input("Nhập mã nhân viên: ").strip(),
            "ten_nv": input("Nhập tên nhân viên: ").strip(),
            "luong_co_ban": float(input("Nhập lương cơ bản: ")),
            "phong_ban": input("Nhập phòng ban: ").strip(),
        }
        return thong_tin

    def them_nhan_vien(self):
        print("\n====== THÊM NHÂN VIÊN ======")
        print("1. Nhân viên văn phòng")
        print("2. Nhân viên kỹ sư")
        print("3. Nhân viên bán hàng")
        print("============================")

        chon = int(input("Nhập lựa chọn của bạn: "))
        thong_tin = self.nhap_thong_tin_chung()
        if chon == 1:
            phu_cap = float(input("Nhập phụ cấp: "))
            nv = NhanVienVanPhong(**thong_tin, phu_cap=phu_cap)
        elif chon == 2:
            tien_du_an = float(input("Nhập tiền từ dự án: "))
            nv = NhanVienKySu(**thong_tin, du_an=tien_du_an)
        elif chon == 3:
            doanh_so = float(input("Nhập doanh số: "))
            hoa_hong = float(input("Nhập hoa hồng (%): "))
            nv = NhanvienBanHang(**thong_tin, doanh_so=doanh_so, hoa_hong=hoa_hong)
        else:
            print("Lựa chọn không hợp lệ")
            return
        self.list_nhan_vien.append(nv)
        print("=> Thêm nhân viên thành công!")

    def hien_thi_danh_sach(self):
        if not self.list_nhan_vien:
            print("\nDanh sách nhân viên đang trống!")
            return
        print("\n===== Danh sách nhân viên =====")
        tong_luong = 0

        for nv in self.list_nhan_vien:
            nv.hien_thi_thong_tin()
            tong_luong += nv.tinh_luong()
        print(f"Tổng lương công ty: {tong_luong:,.0f} VND")

    def menu(self):
        while True:
            print("\n========= QUẢN LÝ NHÂN VIÊN =========")
            print("1. Thêm nhân viên")
            print("2. Hiển thị danh sách nhân viên")
            print("3. Thoát")
            print("====================================")

            chon = int(input("Nhập lựa chọn: "))

            if chon == 1:
                self.them_nhan_vien()
            elif chon == 2:
                self.hien_thi_danh_sach()
            elif chon == 3:
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


qlnv = QuanLyNhanVien()
qlnv.menu()
