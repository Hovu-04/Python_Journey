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

    @abstractmethod
    def loai_nhan_vien(self):
        pass

    @abstractmethod
    def thong_tin_rieng(self):
        pass

    def hien_thi_thong_tin(self):
        print("\n===== THÔNG TIN NHÂN VIÊN =====")
        print(f"Loại NV     : {self.loai_nhan_vien()}")
        print(f"Mã NV       : {self.ma_nv}")
        print(f"Họ tên      : {self.ten_nv}")
        print(f"Phòng ban   : {self.phong_ban}")
        print(f"Lương CB    : {self.luong_co_ban:,.0f} VND")

        for key, value in self.thong_tin_rieng().items():
            print(f"{key:<12}: {value}")

        print(f"Thực lãnh   : {self.tinh_luong():,.0f} VND")
        print("================================")


class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban, phu_cap):
        super().__init__(ma_nv, ten_nv, luong_co_ban, phong_ban)
        self.phu_cap = phu_cap

    def tinh_luong(self):
        return self.luong_co_ban + self.phu_cap

    def loai_nhan_vien(self):
        return "Văn phòng"

    def thong_tin_rieng(self):
        return {"Phụ cấp": f"{self.phu_cap:,.0f} VND"}


class NhanVienKySu(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban, tien_du_an):
        super().__init__(ma_nv, ten_nv, luong_co_ban, phong_ban)
        self.tien_du_an = tien_du_an

    def tinh_luong(self):
        return self.luong_co_ban + self.tien_du_an

    def loai_nhan_vien(self):
        return "Kỹ sư"

    def thong_tin_rieng(self):
        return {"Tiền dự án": f"{self.tien_du_an:,.0f} VND"}


class NhanVienBanHang(NhanVien):
    def __init__(self, ma_nv, ten_nv, luong_co_ban, phong_ban, hoa_hong, doanh_so):
        super().__init__(ma_nv, ten_nv, luong_co_ban, phong_ban)
        self.hoa_hong = hoa_hong
        self.doanh_so = doanh_so

    def tinh_luong(self):
        return self.luong_co_ban + self.doanh_so * (self.hoa_hong / 100)

    def loai_nhan_vien(self):
        return "Bán hàng"

    def thong_tin_rieng(self):
        return {
            "Hoa hồng": f"{self.hoa_hong}%",
            "Doanh số": f"{self.doanh_so:,.0f} VND",
        }


class QuanLyNhanVien:
    def __init__(self):
        self.danh_sach_nv = []

    def nhap_chuoi(self, thong_bao):
        while True:
            gia_tri = input(thong_bao).strip()
            if gia_tri:
                return gia_tri
            print("Không được để trống!")

    def nhap_so(self, thong_bao):
        while True:
            try:
                gia_tri = float(input(thong_bao))
                if gia_tri < 0:
                    print("Vui lòng nhập số >= 0!")
                    continue
                return gia_tri
            except ValueError:
                print("Dữ liệu không hợp lệ, vui lòng nhập số!")

    def tim_nhan_vien_theo_ma(self, ma_nv):
        for nv in self.danh_sach_nv:
            if nv.ma_nv.lower() == ma_nv.lower():
                return nv
        return None

    def nhap_thong_tin_chung(self, cho_phep_trung_ma=False):
        while True:
            ma_nv = self.nhap_chuoi("Nhập mã nhân viên: ")
            if cho_phep_trung_ma or not self.tim_nhan_vien_theo_ma(ma_nv):
                break
            print("Mã nhân viên đã tồn tại, vui lòng nhập mã khác!")

        ten_nv = self.nhap_chuoi("Nhập tên nhân viên: ")
        luong_co_ban = self.nhap_so("Nhập lương cơ bản: ")
        phong_ban = self.nhap_chuoi("Nhập phòng ban: ")

        return {
            "ma_nv": ma_nv,
            "ten_nv": ten_nv,
            "luong_co_ban": luong_co_ban,
            "phong_ban": phong_ban,
        }

    def tao_nhan_vien(self):
        print("\n====== THÊM NHÂN VIÊN ======")
        print("1. Nhân viên văn phòng")
        print("2. Nhân viên kỹ sư")
        print("3. Nhân viên bán hàng")
        print("============================")

        try:
            lua_chon = int(input("Nhập lựa chọn của bạn: "))
        except ValueError:
            print("Lựa chọn không hợp lệ!")
            return None

        thong_tin = self.nhap_thong_tin_chung()

        if lua_chon == 1:
            phu_cap = self.nhap_so("Nhập phụ cấp: ")
            return NhanVienVanPhong(**thong_tin, phu_cap=phu_cap)

        elif lua_chon == 2:
            tien_du_an = self.nhap_so("Nhập tiền dự án: ")
            return NhanVienKySu(**thong_tin, tien_du_an=tien_du_an)

        elif lua_chon == 3:
            hoa_hong = self.nhap_so("Nhập % hoa hồng: ")
            doanh_so = self.nhap_so("Nhập doanh số: ")
            return NhanVienBanHang(**thong_tin, hoa_hong=hoa_hong, doanh_so=doanh_so)

        else:
            print("Lựa chọn không hợp lệ!")
            return None

    def them_nhan_vien(self):
        nv = self.tao_nhan_vien()
        if nv:
            self.danh_sach_nv.append(nv)
            print("=> Thêm nhân viên thành công!")

    def hien_thi_danh_sach(self):
        if not self.danh_sach_nv:
            print("Danh sách nhân viên đang trống!")
            return

        tong_luong = 0
        print("\n=========== DANH SÁCH NHÂN VIÊN ===========")
        for i, nv in enumerate(self.danh_sach_nv, start=1):
            print(f"\n--- Nhân viên {i} ---")
            nv.hien_thi_thong_tin()
            tong_luong += nv.tinh_luong()

        print(f"\nTổng lương công ty: {tong_luong:,.0f} VND")

    def xem_chi_tiet_nhan_vien(self):
        ma_nv = self.nhap_chuoi("Nhập mã nhân viên cần xem: ")
        nv = self.tim_nhan_vien_theo_ma(ma_nv)

        if nv:
            nv.hien_thi_thong_tin()
        else:
            print("Không tìm thấy nhân viên!")

    def cap_nhat_nhan_vien(self):
        ma_nv = self.nhap_chuoi("Nhập mã nhân viên cần sửa: ")
        nv = self.tim_nhan_vien_theo_ma(ma_nv)

        if not nv:
            print("Không tìm thấy nhân viên!")
            return

        print("\nNhập thông tin mới:")
        nv.ten_nv = self.nhap_chuoi("Nhập tên mới: ")
        nv.luong_co_ban = self.nhap_so("Nhập lương cơ bản mới: ")
        nv.phong_ban = self.nhap_chuoi("Nhập phòng ban mới: ")

        if isinstance(nv, NhanVienVanPhong):
            nv.phu_cap = self.nhap_so("Nhập phụ cấp mới: ")

        elif isinstance(nv, NhanVienKySu):
            nv.tien_du_an = self.nhap_so("Nhập tiền dự án mới: ")

        elif isinstance(nv, NhanVienBanHang):
            nv.hoa_hong = self.nhap_so("Nhập % hoa hồng mới: ")
            nv.doanh_so = self.nhap_so("Nhập doanh số mới: ")

        print("=> Cập nhật nhân viên thành công!")

    def xoa_nhan_vien(self):
        ma_nv = self.nhap_chuoi("Nhập mã nhân viên cần xóa: ")
        nv = self.tim_nhan_vien_theo_ma(ma_nv)

        if not nv:
            print("Không tìm thấy nhân viên!")
            return

        self.danh_sach_nv.remove(nv)
        print("=> Xóa nhân viên thành công!")

    def tim_kiem_nhan_vien_theo_ten(self):
        tu_khoa = self.nhap_chuoi("Nhập tên cần tìm: ").lower()
        ket_qua = []

        for nv in self.danh_sach_nv:
            if tu_khoa in nv.ten_nv.lower():
                ket_qua.append(nv)

        if not ket_qua:
            print("Không tìm thấy nhân viên phù hợp!")
            return

        print(f"\nTìm thấy {len(ket_qua)} nhân viên:")
        for nv in ket_qua:
            nv.hien_thi_thong_tin()

    def menu(self):
        while True:
            print("\n============= QUẢN LÝ NHÂN VIÊN =============")
            print("1. Thêm nhân viên")
            print("2. Hiển thị danh sách nhân viên")
            print("3. Xem chi tiết nhân viên theo mã")
            print("4. Cập nhật nhân viên")
            print("5. Xóa nhân viên")
            print("6. Tìm kiếm nhân viên theo tên")
            print("0. Thoát")
            print("=============================================")

            try:
                lua_chon = int(input("Nhập lựa chọn của bạn: "))
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
                continue

            if lua_chon == 1:
                self.them_nhan_vien()
            elif lua_chon == 2:
                self.hien_thi_danh_sach()
            elif lua_chon == 3:
                self.xem_chi_tiet_nhan_vien()
            elif lua_chon == 4:
                self.cap_nhat_nhan_vien()
            elif lua_chon == 5:
                self.xoa_nhan_vien()
            elif lua_chon == 6:
                self.tim_kiem_nhan_vien_theo_ten()
            elif lua_chon == 0:
                print("Thoát chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


if __name__ == "__main__":
    ql = QuanLyNhanVien()
    ql.menu()
