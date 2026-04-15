class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # Gọi setter kiểm tra ngay khi khởi tạo

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        # Sửa điều kiện: chỉ chặn số âm, cho phép số dư = 0
        if value < 0:
            raise ValueError("Số tiền không được là số âm!")
        self._balance = value

    def recharge(self, amount):
        """Nạp tiền vào tài khoản"""
        # Bước 1: Kiểm tra số tiền nạp vào phải dương (Logic nghiệp vụ)
        if amount <= 0:
            print(f"❌ Lỗi: Số tiền nạp ({amount}) phải lớn hơn 0!")
            return  # Thoát hàm ngay, không chạy dòng phía dưới

        # Bước 2: Cập nhật thông qua setter
        self.balance = self.balance + amount
        print(f"✅ Đã nạp thành công {amount:,} VND. Số dư mới: {self.balance:,} VND")

    def withdraw(self, amount):
        """Rút tiền từ tài khoản"""
        print(f"--- Đang thực hiện rút {amount:,} VND ---")
        try:
            # Gọi setter. Nếu (balance - amount) < 0 -> Setter ném lỗi
            self.balance = self.balance - amount
            print(f"✅ Rút thành công. Số dư còn: {self.balance:,} VND")
        except ValueError:
            print(f"❌ Thất bại: Số dư không đủ để rút {amount:,} VND!")


# Kiểm tra các trường hợp:
print("--- Kiểm tra rút tiền hợp lệ ---")
acc = Account("Bạn", 2000000)
acc.recharge(500000)


print("\n--- Kiểm tra rút quá số dư ---")
try:
    acc.withdraw(2000000)  # Cố rút 2tr từ tài khoản còn 1.5tr
except ValueError as e:
    print(f"Bị chặn! Lỗi: {e}")
