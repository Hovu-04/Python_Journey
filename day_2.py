# =========================================
# ! PRODUCT - DOMAIN MODEL
# Quản lý sản phẩm + tồn kho + giá
# =========================================
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        # * STEP 1: Khởi tạo thông tin cơ bản
        self.product_id = product_id
        self.name = name

        # * STEP 2: Gán giá và tồn kho thông qua setter
        # → đảm bảo dữ liệu hợp lệ ngay từ đầu
        self.price = price
        self.stock_quantity = stock_quantity

    # =========================================
    # * PRICE FLOW
    # =========================================
    @property
    def price(self):
        # * STEP 3: Khi truy cập → trả về giá đã validate
        return self._price

    @price.setter
    def price(self, value):
        # * STEP 4: Khi gán → kiểm tra hợp lệ
        if value < 0:
            raise ValueError("Giá sản phẩm không thể âm")
        self._price = value

    # =========================================
    # * STOCK FLOW
    # =========================================
    @property
    def stock_quantity(self):
        # * STEP 5: Lấy tồn kho hiện tại
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        # * STEP 6: Kiểm tra tồn kho không âm
        if value < 0:
            raise ValueError("Tồn kho không thể âm")
        self._stock_quantity = value

    # =========================================
    # ! BUSINESS FLOW: CẬP NHẬT KHO
    # =========================================
    def update_stock(self, quantity_change):
        """
        FLOW:
        1. Nhận số lượng thay đổi (có thể + hoặc -)
        2. Tính tồn kho mới
        3. Validate business rule (không được âm)
        4. Gán lại qua setter → đảm bảo consistency
        """

        # * STEP 7: Tính tồn kho mới
        new_quantity = self.stock_quantity + quantity_change

        # * STEP 8: Validate nghiệp vụ (không bán quá số lượng)
        if new_quantity < 0:
            raise ValueError("Không đủ hàng trong kho")

        # * STEP 9: Gán qua setter (double-check validation)
        self.stock_quantity = new_quantity

        print(f"[{self.name}] Tồn kho mới: {self.stock_quantity}")

    # =========================================
    # * DISPLAY FLOW (demo)
    # =========================================
    def display_info(self):
        # * STEP 10: Truy cập qua getter để đảm bảo dữ liệu hợp lệ
        print(
            f"{self.product_id} | {self.name} | {self.price:,.0f} VND | SL: {self.stock_quantity}"
        )


# =========================================
# ! TEST FLOW - MÔ PHỎNG THỰC TẾ
# =========================================

# STEP A: Tạo sản phẩm → chạy qua __init__ → setter validate
laptop = Product("LAP001", "Laptop Dell XPS 13", 25_000_000, 10)

# STEP B: Hiển thị thông tin ban đầu
laptop.display_info()

# STEP C: Bán hàng (giảm tồn kho)
laptop.update_stock(-3)

# STEP D: Nhập hàng (tăng tồn kho)
laptop.update_stock(5)

# STEP E: Thay đổi giá (qua setter)
laptop.price = 23_500_000

# STEP F: Hiển thị lại trạng thái cuối
laptop.display_info()
