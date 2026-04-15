class Product:
    # Phương thức __init__ để khởi tạo đối tượng
    def __init__(self, product_id, name, price, stock_quantity):
        # Gán giá trị cho các thuộc tính của đối tượng sử dụng 'self'
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    # Phương thức display_info để hiển thị thông tin sản phẩm
    # Luôn nhận 'self' để truy cập các thuộc tính của đối tượng
    def display_info(self):
        print(f"--- Thông tin Sản phẩm ---")
        print(f"Mã SP: {self.product_id}")
        print(f"Tên SP: {self.name}")
        print(f"Giá: {self.price:.2f} VNĐ")  # Định dạng giá cho đẹp
        print(f"Số lượng tồn: {self.stock_quantity}")
        print(f"------------------------")


# --- Phần thực hành ---

# 1. Tạo các đối tượng (instances) của class Product
# Khi bạn gọi Product(...), __init__ sẽ tự động được gọi
laptop = Product("LAP001", "Laptop Dell XPS 13", 25000000, 10)
dien_thoai = Product("PHONE005", "iPhone 15 Pro", 30000000, 5)
sach = Product("BOOK010", "Python Crash Course", 350000, 50)

# 2. Gọi phương thức display_info() trên các đối tượng
laptop.display_info()
dien_thoai.display_info()
sach.display_info()

# Bạn có thể truy cập trực tiếp các thuộc tính nếu muốn (chưa áp dụng đóng gói)
print(f"\nGiá của laptop: {laptop.price} VNĐ")
