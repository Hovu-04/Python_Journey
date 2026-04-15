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

    @page_count.setter
    def add_pages(self, extra_pages):
        newValue = self.page_count + extra_pages
        if newValue <= 0:
            raise ValueError("Số trang phải là số nguyên lớn hơn 0")
        self.page_count = newValue

    @page_count.setter
    def remove_pages(self, remove_pages):
        newValue = self.page_count - remove_pages
        self.page_count = newValue


sach_1 = Book("B001", "Dế Mèn Phiêu Lưu Ký", "Tô Hoài", 300)
sach_1.remove_pages = 50
sach_1.display_book_info()
