# =========================================
# ! BOOK - DOMAIN MODEL
# Quản lý thông tin sách + số trang
# =========================================
class Book:
    def __init__(self, book_id, title, author, page_count):
        # * STEP 1: Gán thông tin cơ bản
        self.book_id = book_id
        self.title = title
        self.author = author

        # * STEP 2: Gán số trang qua setter → đảm bảo hợp lệ ngay từ đầu
        self.page_count = page_count

    # =========================================
    # * PAGE COUNT FLOW
    # =========================================
    @property
    def page_count(self):
        # * STEP 3: Khi truy cập → trả về giá trị đã validate
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # * STEP 4: Validate dữ liệu (rule cốt lõi)
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Số trang phải là số nguyên > 0")

        self._page_count = value

    # =========================================
    # ! BUSINESS FLOW: THÊM TRANG
    # =========================================
    def add_pages(self, extra_pages):
        """
        FLOW:
        1. Nhận số trang cần thêm
        2. Validate input
        3. Tính tổng mới
        4. Gán qua setter (double-check)
        """

        # * STEP 5: Validate input
        if extra_pages <= 0:
            raise ValueError("Số trang thêm phải > 0")

        # * STEP 6: Cập nhật qua setter
        self.page_count = self.page_count + extra_pages

        print(f"Đã cộng thêm {extra_pages} trang cho '{self.title}'")

    # =========================================
    # ! BUSINESS FLOW: GIẢM TRANG
    # =========================================
    def remove_pages(self, pages):
        """
        FLOW:
        1. Nhận số trang cần giảm
        2. Validate input
        3. Kiểm tra không được <= 0
        4. Gán qua setter
        """

        # * STEP 7: Validate input
        if pages <= 0:
            raise ValueError("Số trang giảm phải > 0")

        new_total = self.page_count - pages

        # ! STEP 8: Rule nghiệp vụ (không được <= 0 trang)
        if new_total <= 0:
            raise ValueError("Không thể giảm trang khiến sách không hợp lệ")

        # * STEP 9: Gán qua setter
        self.page_count = new_total

        print(f"Đã trừ {pages} trang cho '{self.title}'")

    # =========================================
    # * DISPLAY FLOW (demo)
    # =========================================
    def display_book_info(self):
        # * STEP 10: Hiển thị thông tin (dùng getter)
        print(f"--- Thông tin Sách ---")
        print(f"Mã sách: {self.book_id}")
        print(f"Tên sách: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Số trang: {self.page_count}")
        print(f"---------------------")


# =========================================
# ! TEST FLOW
# =========================================

# STEP A: Khởi tạo sách → validate page_count
sach1 = Book("B001", "Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 300)

# STEP B: Thêm trang
sach1.add_pages(20)

# STEP C: Giảm trang hợp lệ
sach1.remove_pages(10)

# STEP D: Hiển thị kết quả
sach1.display_book_info()
