class Sach:
    def __init__(self, ma_sach, ten_sach, gia_ban, so_luong):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.gia_ban = gia_ban
        self.so_luong = so_luong

    def show_info_book(self):
        print("===== Thông tin sách =====")
        print(f"Mã sách: {self.ma_sach}")
        print(f"Tên sách: {self.ten_sach}")
        print(f"Giá bán: {self.gia_ban:,d} VND")
        print(f"Số lượng: {self.so_luong}")
        print("==========================")


class QuanLySach:
    def __init__(self):
        self.list_sach = []

    def add_new_book(self, ma_sach, ten_sach, gia_ban, so_luong):
        if ma_sach is None or ten_sach is None:
            print("Nhập đầy đủ thông tin!")
            return
        if gia_ban <= 0 or so_luong <= 0:
            print("Giá bán và số lượng phải lớn hơn 0!")
            return
        sach_moi = Sach(ma_sach, ten_sach, gia_ban, so_luong)
        self.list_sach.append(sach_moi)
        print(f"Thêm sách {ten_sach} thành công!")

    def remove_book_id(self, ma_sach_can_tim=""):
        for book in self.list_sach:
            if book.ma_sach == ma_sach_can_tim:
                self.list_sach.remove(book)
                print(f"Xóa sách có mã {ma_sach_can_tim} thành công!")
                return

    def show_all_book(self):
        if not self.list_sach:
            print("Danh sách không được trống!")
            return
        for book in self.list_sach:
            book.show_info_book()


qls = QuanLySach()

qls.add_new_book("BK_01", "Nuốt ngược nước mắt để trưởng thành", 100000, 40)
qls.add_new_book("BK_02", "Thay đổi nhỏ thành công lớn", 80000, 90)
qls.add_new_book("BK_03", "Thói quen kỷ luật bản thân", 50000, 20)
qls.add_new_book("BK_04", "Học lập trình căn bản với python", 50000, 20)
qls.remove_book_id("BK_02")
# qls.show_all_book()
