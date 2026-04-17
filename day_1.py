# =========================================
# ! PRODUCT - DOMAIN MODEL
# Đại diện cho một sản phẩm trong hệ thống
# =========================================
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        # * Validate dữ liệu đầu vào (tránh rác)
        if price < 0:
            raise ValueError("Giá không được âm!")
        if stock_quantity < 0:
            raise ValueError("Số lượng tồn không được âm!")

        self.product_id = product_id
        self.name = name
        self._price = price  # ! dùng _ để chuẩn bị encapsulation
        self._stock_quantity = stock_quantity

    # =========================================
    # * PROPERTY: price (có kiểm soát)
    # =========================================
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Giá không hợp lệ!")
        self._price = value

    # =========================================
    # * PROPERTY: stock_quantity
    # =========================================
    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if value < 0:
            raise ValueError("Số lượng tồn không hợp lệ!")
        self._stock_quantity = value

    # =========================================
    # * BUSINESS LOGIC: bán hàng
    # =========================================
    def sell(self, quantity):
        if quantity <= 0:
            raise ValueError("Số lượng bán phải > 0")

        if quantity > self._stock_quantity:
            raise ValueError("Không đủ hàng trong kho")

        self._stock_quantity -= quantity

    # =========================================
    # * HIỂN THỊ (UI - demo)
    # =========================================
    def display_info(self):
        print(f"--- Thông tin Sản phẩm ---")
        print(f"Mã SP: {self.product_id}")
        print(f"Tên SP: {self.name}")
        print(f"Giá: {self._price:,.0f} VNĐ")
        print(f"Số lượng tồn: {self._stock_quantity}")
        print(f"------------------------")


# =========================================
# ! TEST FLOW
# =========================================
laptop = Product("LAP001", "Laptop Dell XPS 13", 25_000_000, 10)

# * Bán hàng
laptop.sell(2)

# * Hiển thị
laptop.display_info()

# * Truy cập qua property
print(f"\nGiá laptop: {laptop.price:,} VNĐ")
