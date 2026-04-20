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
        print("\n===== DANH SÁCH NHÂN VIÊN =====")
        print(f"Mã NV      : {self.ma_nv}")
        print(f"Họ tên     : {self.ten_nv}")
        print(f"Phòng ban  : {self.phong_ban}")
        print(f"Lương CB   : {self.luong_co_ban:,} VND")
        print(f"Thực lãnh  : {self.tinh_luong():,} VND")
        print("=================================")


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


class NhanVienBanHang(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban, hoa_hong, doanh_so):
        super().__init__(ma_nv, ten_nv, luong_co_ban, phong_ban)
        self.hoa_hong = hoa_hong
        self.doanh_so = doanh_so

    def tinh_luong(self):
        return self.luong_co_ban + self.doanh_so * (self.hoa_hong / 100)


class QuanLyNhanVien:
    def __init__(self):
        self.list_danh_sach_nv = []

    def nhap_thong_tin_chung(self):
        thong_tin = {
            "ma_nv": input("Nhập mã nhân viên: ").strip(),
            "ten_nv": input("Nhập tên nhân viên: ").strip(),
            "luong_co_ban": float(input("Nhập lương cơ bản: ")),
            "phong_ban": input("Nhập tên phòng ban: ").strip(),
        }
        return thong_tin

    def them_thong_tin_nv(self):
        print("\n====== THÊM NHÂN VIÊN ======")
        print("1. Nhân viên văn phòng")
        print("2. Nhân viên kỹ sư")
        print("3. Nhân viên bán hàng")
        print("============================")

        lua_chon = int(input("Nhập lựa chọn của bạn: "))
        thong_tin = self.nhap_thong_tin_chung()

        if lua_chon == 1:
            phu_cap = float(input("Nhập phụ cấp: "))
            nv = NhanVienVanPhong(**thong_tin, phu_cap=phu_cap)
        elif lua_chon == 2:
            tien_du_an = float(input("Nhập số tiền dự án: "))
            nv = NhanVienKySu(**thong_tin, du_an=tien_du_an)
        elif lua_chon == 3:
            hoa_hong = float(input("Nhập hoa hồng: "))
            doanh_so = float(input("Nhập doanh số: "))
            nv = NhanVienBanHang(**thong_tin, hoa_hong=hoa_hong, doanh_so=doanh_so)
        else:
            print("Lựa chọn không hợp lệ!")
            return
        self.list_danh_sach_nv.append(nv)
        print("=> Thêm nhân viên thành công!")

    def hien_thi_thong_tin_nv(self):
        if not self.list_danh_sach_nv:
            print("Danh sách nhân viên đang trống!")
            return

        tong_luong = 0
        for nv in self.list_danh_sach_nv:
            nv.hien_thi_thong_tin()
            tong_luong += nv.tinh_luong()
        print(f"Tổng lương của công ty: {tong_luong:,} VNĐ")

    def menu(self):
        while True:
            print("\n========= QUẢN LÝ NHÂN VIÊN =========")
            print("1. Thêm nhân viên")
            print("2. Hiện thị danh sách nhân viên")
            print("3. Thoát")

            lua_chon = int(input("Nhập lựa chọn của bạn: "))

            if lua_chon == 1:
                self.them_thong_tin_nv()
            elif lua_chon == 2:
                self.hien_thi_thong_tin_nv()
            elif lua_chon == 3:
                print("Thoát chương trình!")
                break
            else:
                print("lựa chọn không hợp lệ, vui lòng nhập lại!")
                break


ql = QuanLyNhanVien()
ql.menu()
