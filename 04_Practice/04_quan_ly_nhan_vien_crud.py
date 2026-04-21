# ! ABSTRACT BASE CLASS:
# NOTE: Đây là lớp cha trừu tượng, dùng làm khung chuẩn cho mọi loại nhân viên.
# NOTE: Mọi class con kế thừa từ đây bắt buộc phải tự định nghĩa cách tính lương
# NOTE: và thông tin riêng của từng loại nhân viên.

from abc import ABC, abstractmethod


class NhanVien(ABC):
    def __init__(self, ma_nv, ten_nv, luong_cb, phong_ban):
        # * INIT FLOW:
        # 1. Nhận dữ liệu đầu vào khi tạo object nhân viên
        # 2. Chuẩn hóa mã nhân viên
        # 3. Gán dữ liệu thông qua property để đi qua lớp kiểm tra hợp lệ
        self._ma_nv = ma_nv.strip().upper()
        self.ten_nv = ten_nv
        self.luong_cb = luong_cb
        self.phong_ban = phong_ban

    @property
    def ma_nv(self):
        # * GETTER FLOW: trả về mã nhân viên đã được chuẩn hóa
        return self._ma_nv

    @property
    def ten_nv(self):
        # * GETTER FLOW: trả về tên nhân viên
        return self._ten_nv

    @ten_nv.setter
    def ten_nv(self, value):
        # * SETTER FLOW:
        # 1. Loại bỏ khoảng trắng dư
        # 2. Kiểm tra tên có rỗng hay không
        # 3. Chuẩn hóa kiểu hiển thị tên
        value = value.strip()
        if not value:
            raise ValueError("Tên nhân viên không được để trống!")
        self._ten_nv = value.title()

    @property
    def luong_cb(self):
        # * GETTER FLOW: trả về lương cơ bản
        return self._luong_cb

    @luong_cb.setter
    def luong_cb(self, value):
        # * SETTER FLOW:
        # 1. Kiểm tra lương không được âm
        # 2. Ép kiểu về float để tính toán thống nhất
        if value is None or value < 0:
            raise ValueError("Lương cơ bản không được âm!")
        self._luong_cb = float(value)

    @property
    def phong_ban(self):
        # * GETTER FLOW: trả về tên phòng ban
        return self._phong_ban

    @phong_ban.setter
    def phong_ban(self, value):
        # * SETTER FLOW:
        # 1. Chuẩn hóa chuỗi
        # 2. Kiểm tra phòng ban không được rỗng
        value = value.strip()
        if not value:
            raise ValueError("Phòng ban không được để trống!")
        self._phong_ban = value.title()

    @abstractmethod
    def tinh_luong(self):
        # ! ABSTRACT METHOD:
        # NOTE: Mỗi loại nhân viên phải tự định nghĩa công thức tính lương riêng
        pass

    @abstractmethod
    def thong_tin_rieng(self):
        # ! ABSTRACT METHOD:
        # NOTE: Mỗi loại nhân viên phải tự trả về thông tin đặc thù của mình
        pass

    def hien_thi_thong_tin(self):
        # * OUTPUT FLOW:
        # 1. In thông tin chung của nhân viên
        # 2. Gọi đa hình tới thong_tin_rieng()
        # 3. Gọi đa hình tới tinh_luong()
        print("\n===== THÔNG TIN NHÂN VIÊN =====")
        print(f"Mã NV       : {self.ma_nv}")
        print(f"Họ tên      : {self.ten_nv}")
        print(f"Phòng ban   : {self.phong_ban}")
        print(f"Lương CB    : {self.luong_cb:,.0f} VND")
        print(self.thong_tin_rieng())
        print(f"Thực lãnh   : {self.tinh_luong():,.0f} VND")
        print("================================")


class NhanVienVanPhong(NhanVien):
    # ! CHILD CLASS:
    # NOTE: Kế thừa toàn bộ dữ liệu chung từ NhanVien
    # NOTE: Thêm thuộc tính riêng là phụ cấp

    def __init__(self, ma_nv, ten_nv, luong_cb, phong_ban, phu_cap):
        # * INIT FLOW:
        # 1. Gọi constructor lớp cha để khởi tạo dữ liệu chung
        # 2. Gán thêm thuộc tính riêng của nhân viên văn phòng
        super().__init__(ma_nv, ten_nv, luong_cb, phong_ban)
        self.phu_cap = phu_cap

    @property
    def phu_cap(self):
        # * GETTER FLOW: trả về phụ cấp
        return self._phu_cap

    @phu_cap.setter
    def phu_cap(self, value):
        # * SETTER FLOW: phụ cấp không được âm
        if value is None or value < 0:
            raise ValueError("Phụ cấp không được âm!")
        self._phu_cap = float(value)

    def tinh_luong(self):
        # * BUSINESS LOGIC:
        # Lương nhân viên văn phòng = lương cơ bản + phụ cấp
        return self.luong_cb + self.phu_cap

    def thong_tin_rieng(self):
        # * OUTPUT FLOW: trả về thông tin riêng để lớp cha hiển thị
        return f"Phụ cấp     : {self.phu_cap:,.0f} VND"


class NhanVienKySu(NhanVien):
    # ! CHILD CLASS:
    # NOTE: Kế thừa dữ liệu chung và thêm tiền dự án

    def __init__(self, ma_nv, ten_nv, luong_cb, phong_ban, tien_du_an):
        # * INIT FLOW:
        # 1. Khởi tạo phần chung
        # 2. Gán thêm tiền dự án
        super().__init__(ma_nv, ten_nv, luong_cb, phong_ban)
        self.tien_du_an = tien_du_an

    @property
    def tien_du_an(self):
        # * GETTER FLOW: trả về tiền dự án
        return self._tien_du_an

    @tien_du_an.setter
    def tien_du_an(self, value):
        # * SETTER FLOW: tiền dự án không được âm
        if value is None or value < 0:
            raise ValueError("Tiền dự án không được âm!")
        self._tien_du_an = float(value)

    def tinh_luong(self):
        # * BUSINESS LOGIC:
        # Lương kỹ sư = lương cơ bản + tiền dự án
        return self.luong_cb + self.tien_du_an

    def thong_tin_rieng(self):
        # * OUTPUT FLOW: trả về thông tin đặc thù của kỹ sư
        return f"Tiền dự án  : {self.tien_du_an:,.0f} VND"


class NhanVienBanHang(NhanVien):
    # ! CHILD CLASS:
    # NOTE: Kế thừa dữ liệu chung và thêm doanh số + hoa hồng

    def __init__(self, ma_nv, ten_nv, luong_cb, phong_ban, doanh_so, hoa_hong):
        # * INIT FLOW:
        # 1. Khởi tạo phần chung
        # 2. Gán doanh số và tỷ lệ hoa hồng
        super().__init__(ma_nv, ten_nv, luong_cb, phong_ban)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    @property
    def doanh_so(self):
        # * GETTER FLOW: trả về doanh số
        return self._doanh_so

    @doanh_so.setter
    def doanh_so(self, value):
        # * SETTER FLOW: doanh số không được âm
        if value is None or value < 0:
            raise ValueError("Doanh số không được âm!")
        self._doanh_so = float(value)

    @property
    def hoa_hong(self):
        # * GETTER FLOW: trả về phần trăm hoa hồng
        return self._hoa_hong

    @hoa_hong.setter
    def hoa_hong(self, value):
        # * SETTER FLOW:
        # 1. Hoa hồng không được âm
        # 2. Hoa hồng không vượt quá 100%
        if value is None or value < 0 or value > 100:
            raise ValueError("Hoa hồng phải từ 0 đến 100!")
        self._hoa_hong = float(value)

    def tinh_luong(self):
        # * BUSINESS LOGIC:
        # Lương bán hàng = lương cơ bản + tiền hoa hồng theo doanh số
        return self.luong_cb + (self.doanh_so * self.hoa_hong / 100)

    def thong_tin_rieng(self):
        # * OUTPUT FLOW:
        # Trả về nhiều dòng thông tin riêng của nhân viên bán hàng
        return (
            f"Doanh số    : {self.doanh_so:,.0f} VND\n"
            f"Hoa hồng    : {self.hoa_hong:.2f} %"
        )


class QuanLyNhanVien:
    # ! MANAGER CLASS:
    # NOTE: Lớp này chịu trách nhiệm quản lý danh sách nhân viên
    # NOTE: Bao gồm thêm, tìm, sửa, xóa, hiển thị và menu điều khiển

    def __init__(self):
        # * INIT FLOW: tạo danh sách rỗng để lưu object nhân viên
        self.danh_sach_nv = []

    def nhap_chuoi(self, thong_bao, mac_dinh=None):
        # * INPUT FLOW:
        # 1. Hiển thị thông báo nhập chuỗi
        # 2. Nếu người dùng bỏ trống:
        #    - trả về mặc định nếu có
        #    - báo lỗi nếu không có mặc định
        while True:
            gia_tri = input(thong_bao).strip()
            if not gia_tri:
                if mac_dinh is not None:
                    return mac_dinh
                print("Không được để trống!")
                continue
            return gia_tri

    def nhap_so(self, thong_bao, mac_dinh=None, min_value=0):
        # * INPUT FLOW:
        # 1. Hiển thị yêu cầu nhập số
        # 2. Kiểm tra dữ liệu có phải số hay không
        # 3. Kiểm tra số có đạt ngưỡng min_value hay không
        while True:
            gia_tri = input(thong_bao).strip()
            if not gia_tri:
                if mac_dinh is not None:
                    return mac_dinh
                print("Không được để trống!")
                continue
            try:
                so = float(gia_tri)
                if so < min_value:
                    print(f"Vui lòng nhập số >= {min_value}!")
                    continue
                return so
            except ValueError:
                print("Dữ liệu không hợp lệ, vui lòng nhập số!")

    def tim_nhan_vien_theo_ma(self, ma_nv):
        # * SEARCH FLOW:
        # 1. Chuẩn hóa mã nhập vào
        # 2. Duyệt toàn bộ danh sách nhân viên
        # 3. So sánh mã
        # 4. Trả về object nếu tìm thấy, ngược lại trả về None
        ma_nv = ma_nv.strip().lower()
        for nv in self.danh_sach_nv:
            if nv.ma_nv.lower() == ma_nv:
                return nv
        return None

    def tim_kiem_nhan_vien_theo_ten(self):
        # * SEARCH FLOW:
        # 1. Nhập từ khóa tên cần tìm
        # 2. Duyệt danh sách nhân viên
        # 3. Lọc những nhân viên chứa từ khóa trong tên
        # 4. Hiển thị kết quả
        tu_khoa = self.nhap_chuoi("Nhập tên nhân viên cần tìm: ").lower()
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

    def nhap_thong_tin_chung(self):
        # * INPUT FLOW:
        # 1. Nhập mã nhân viên
        # 2. Kiểm tra mã có bị trùng hay không
        # 3. Nhập tiếp tên, lương cơ bản, phòng ban
        # 4. Trả về dict để dùng chung cho nhiều loại nhân viên
        while True:
            ma_nv = self.nhap_chuoi("Nhập mã nhân viên: ").upper()
            if self.tim_nhan_vien_theo_ma(ma_nv):
                print("Mã nhân viên đã tồn tại, vui lòng nhập mã khác!")
            else:
                break

        ten_nv = self.nhap_chuoi("Nhập tên nhân viên: ")
        luong_cb = self.nhap_so("Nhập lương cơ bản: ")
        phong_ban = self.nhap_chuoi("Nhập phòng ban: ")

        return {
            "ma_nv": ma_nv,
            "ten_nv": ten_nv,
            "luong_cb": luong_cb,
            "phong_ban": phong_ban,
        }

    def tao_nhan_vien(self):
        # * CREATE FLOW:
        # 1. Hiển thị menu chọn loại nhân viên
        # 2. Nhập thông tin chung
        # 3. Tùy loại nhân viên mà nhập thêm thông tin riêng
        # 4. Tạo object tương ứng và trả về
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

        try:
            thong_tin = self.nhap_thong_tin_chung()

            if lua_chon == 1:
                phu_cap = self.nhap_so("Nhập phụ cấp: ")
                return NhanVienVanPhong(**thong_tin, phu_cap=phu_cap)

            elif lua_chon == 2:
                tien_du_an = self.nhap_so("Nhập tiền dự án: ")
                return NhanVienKySu(**thong_tin, tien_du_an=tien_du_an)

            elif lua_chon == 3:
                doanh_so = self.nhap_so("Nhập doanh số: ")
                hoa_hong = self.nhap_so("Nhập hoa hồng (%): ", min_value=0)
                return NhanVienBanHang(
                    **thong_tin, doanh_so=doanh_so, hoa_hong=hoa_hong
                )

            else:
                print("Lựa chọn không hợp lệ!")
                return None

        except ValueError as e:
            print(f"Lỗi: {e}")
            return None

    def them_nhan_vien(self):
        # * CREATE FLOW:
        # 1. Gọi hàm tạo nhân viên
        # 2. Nếu tạo thành công thì thêm vào danh sách
        nv = self.tao_nhan_vien()
        if nv:
            self.danh_sach_nv.append(nv)
            print("=> Thêm nhân viên thành công!")

    def hien_thi_danh_sach(self):
        # * OUTPUT FLOW:
        # 1. Kiểm tra danh sách có rỗng không
        # 2. Duyệt từng nhân viên để hiển thị
        # 3. Đồng thời cộng tổng lương công ty
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
        # * DETAIL FLOW:
        # 1. Nhập mã nhân viên
        # 2. Tìm nhân viên theo mã
        # 3. Nếu có thì hiển thị chi tiết, không có thì báo lỗi
        ma_nv = self.nhap_chuoi("Nhập mã nhân viên cần xem: ").upper()
        nv = self.tim_nhan_vien_theo_ma(ma_nv)

        if nv:
            nv.hien_thi_thong_tin()
        else:
            print("Không tìm thấy nhân viên!")

    def cap_nhat_nhan_vien(self):
        # * UPDATE FLOW:
        # 1. Nhập mã nhân viên cần sửa
        # 2. Tìm đúng object trong danh sách
        # 3. Cho phép nhập mới hoặc giữ nguyên bằng Enter
        # 4. Cập nhật cả dữ liệu chung và dữ liệu riêng theo từng loại nhân viên
        ma_nv = self.nhap_chuoi("Nhập mã nhân viên cần sửa: ").upper()
        nv = self.tim_nhan_vien_theo_ma(ma_nv)

        if not nv:
            print("Không tìm thấy nhân viên!")
            return

        print("\nNhập thông tin mới (Enter để giữ nguyên):")

        try:
            nv.ten_nv = self.nhap_chuoi(f"Tên [{nv.ten_nv}]: ", nv.ten_nv)
            nv.luong_cb = self.nhap_so(f"Lương CB [{nv.luong_cb}]: ", nv.luong_cb)
            nv.phong_ban = self.nhap_chuoi(
                f"Phòng ban [{nv.phong_ban}]: ", nv.phong_ban
            )

            if isinstance(nv, NhanVienVanPhong):
                nv.phu_cap = self.nhap_so(f"Phụ cấp [{nv.phu_cap}]: ", nv.phu_cap)

            elif isinstance(nv, NhanVienKySu):
                nv.tien_du_an = self.nhap_so(
                    f"Tiền dự án [{nv.tien_du_an}]: ", nv.tien_du_an
                )

            elif isinstance(nv, NhanVienBanHang):
                nv.doanh_so = self.nhap_so(f"Doanh số [{nv.doanh_so}]: ", nv.doanh_so)
                nv.hoa_hong = self.nhap_so(
                    f"Hoa hồng (%) [{nv.hoa_hong}]: ", nv.hoa_hong
                )

            print("=> Cập nhật nhân viên thành công!")

        except ValueError as e:
            print(f"Lỗi: {e}")

    def xoa_nhan_vien(self):
        # * DELETE FLOW:
        # 1. Nhập mã nhân viên cần xóa
        # 2. Tìm đúng nhân viên
        # 3. Nếu có thì xóa khỏi danh sách
        ma_nv = self.nhap_chuoi("Nhập mã nhân viên cần xóa: ").upper()
        nv = self.tim_nhan_vien_theo_ma(ma_nv)

        if not nv:
            print("Không tìm thấy nhân viên cần xóa!")
            return

        self.danh_sach_nv.remove(nv)
        print("=> Xóa nhân viên thành công!")

    def menu(self):
        # * MAIN LOOP FLOW:
        # 1. Hiển thị menu chức năng
        # 2. Nhận lựa chọn người dùng
        # 3. Gọi hàm tương ứng
        # 4. Lặp lại cho tới khi chọn thoát
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
    # * PROGRAM START FLOW:
    # 1. Tạo đối tượng quản lý nhân viên
    # 2. Thêm dữ liệu mẫu ban đầu
    # 3. Chạy menu để người dùng thao tác
    ql = QuanLyNhanVien()

    ql.danh_sach_nv.append(
        NhanVienVanPhong("VP01", "nguyễn văn a", 8000000, "hành chính", 2000000)
    )
    ql.danh_sach_nv.append(
        NhanVienKySu("KS01", "trần thị b", 12000000, "kỹ thuật", 5000000)
    )
    ql.danh_sach_nv.append(
        NhanVienBanHang("BH01", "lê văn c", 7000000, "kinh doanh", 300000000, 2)
    )
    ql.danh_sach_nv.append(
        NhanVienBanHang("BH02", "phạm thị d", 7000000, "kinh doanh", 500000000, 3)
    )
    ql.danh_sach_nv.append(
        NhanVienVanPhong("VP02", "hoàng văn e", 9000000, "kế toán", 1500000)
    )

    ql.menu()
