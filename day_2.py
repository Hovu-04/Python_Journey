class Product:
    # Phương thức __init__ để khởi tạo đối tượng
    def __init__(self, product_id, name, price, stock_quantity):
        # Gán giá trị cho các thuộc tính của đối tượng sử dụng 'self'
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    # --- Getter cho price ---
    @property
    def price(self):
        """Getter cho thuộc tính price"""
        # Lấy giá trị đã được lưu trữ (thường là trong một thuộc tính private có tên khác)
        return self._price

    # --- Setter cho price ---
    @price.setter
    def price(self, value):
        """Setter cho thuộc tính price, kiểm tra giá trị trước khi gán"""
        if value < 0:
            # Nếu giá trị không hợp lệ, ném ra một lỗi
            raise ValueError("Giá sản phẩm không thể là số âm.")
        # Nếu giá trị hợp lệ, gán vào thuộc tính private
        self._price = value

    # --- Getter cho stock_quantity ---
    @property
    def stock_quantity(self):
        """Getter cho thuộc tính stock_quantity"""
        return self._stock_quantity

    # --- Setter cho stock_quantity ---
    @stock_quantity.setter
    def stock_quantity(self, value):
        if value < 0:
            raise ValueError("Số lượng tồn kho không thể là số âm.")
        self._stock_quantity = value

    # Phương thức display_info - vẫn tương tự
    def display_info(self):
        print(f"--- Thông tin Sản phẩm ---")
        print(f"Mã SP: {self.product_id}")
        print(f"Tên SP: {self.name}")
        # Khi truy cập self.price ở đây, nó sẽ gọi getter @property price
        print(f"Giá: {self.price:.2f} VNĐ")
        print(
            f"Số lượng tồn: {self.stock_quantity}"
        )  # Truy cập stock_quantity cũng qua getter
        print(f"------------------------")

    # --- Thêm phương thức mới để kiểm tra đóng gói ---
    def update_stock(self, quantity_change):
        """
        Cập nhật số lượng tồn kho.
        quantity_change có thể là số dương (thêm hàng) hoặc số âm (bán hàng).
        Sử dụng setter để đảm bảo số lượng luôn hợp lệ.
        """
        # setter của stock_quantity sẽ tự động kiểm tra giá trị mới
        self.stock_quantity = self.stock_quantity + quantity_change
        print(
            f"Đã cập nhật số lượng tồn kho cho '{self.name}'. Số lượng mới: {self.stock_quantity}"
        )


# --- Phần thực hành ---
# 1. Tạo sản phẩm với giá/số lượng hợp lệ
laptop = Product("LAP001", "Laptop Dell XPS 13", 25000000, 10)
laptop.display_info()

# 2. Thử cập nhật số lượng bằng phương thức update_stock
laptop.update_stock(-3)  # Bán 3 cái
laptop.display_info()

laptop.update_stock(5)  # Nhập thêm 5 cái
laptop.display_info()

# 3. Thử thay đổi giá trực tiếp thông qua setter (sử dụng cú pháp truy cập thuộc tính bình thường)
print("\nThử thay đổi giá sản phẩm:")
laptop.price = 23500000  # Giá mới, hợp lệ
laptop.display_info()

# 4. Thử gán giá trị không hợp lệ để xem lỗi
print("\nThử gán giá không hợp lệ:")
try:
    laptop.price = -5000000  # Giá âm
except ValueError as e:
    print(f"Lỗi: {e}")

try:
    laptop.stock_quantity = -2  # Số lượng tồn âm
except ValueError as e:
    print(f"Lỗi: {e}")

# Thử thay đổi giá trị không hợp lệ thông qua update_stock
print("\nThử cập nhật số lượng không hợp lệ:")
try:
    laptop.update_stock(-15)  # Cố gắng bán nhiều hơn số lượng có
except ValueError as e:
    print(f"Lỗi: {e}")
