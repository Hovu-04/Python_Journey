class Book:
    def __init__(self, book_id, title, author, page_count):
        self.book_id = book_id
        self.title = title
        self.author = author
        # Gọi setter để kiểm tra giá trị ban đầu
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Số trang phải là số nguyên lớn hơn 0")
        self._page_count = value

    def display_book_info(self):
        print(f"--- Thông tin Sách ---")
        print(f"Mã sách: {self.book_id}")
        print(f"Tên sách: {self.title}")
        print(f"Tác giả: {self.author}")
        print(f"Số trang: {self.page_count}")
        print(f"---------------------")

    def add_pages(self, extra_pages):
        self.page_count = self.page_count + extra_pages
        print(f"Đã cộng thêm {extra_pages} trang cho sách '{self.title}'")

    def remove_pages(self, remove_pages):
        self.page_count = self.page_count - remove_pages
        print(f"Đã trừ bớt {remove_pages} trang cho sách '{self.title}'")


# Thử gọi phương thức
sach1 = Book("B001", "Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 300)
sach1.add_pages(20)
sach1.remove_pages(10)
sach1.display_book_info()
