class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    # Phương thức nạp tiền
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền nạp phải lớn hơn 0!")
        self._balance += amount
        print(
            f"[{self._owner}] Nạp thành công: {amount:,.0f} VND | Số dư mới: {self._balance:,.0f} VND"
        )

    # Rút tiền
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0!")
        if amount > self._balance:
            print(
                f"[{self._owner}] Lỗi: Thất bại! Không được rút quá số dư ({amount:,.0f} > {self._balance:,.0f})"
            )
        else:
            self._balance -= amount
            print(
                f"[{self._owner}] Rút thành công: {amount:,.0f} VND | Số dư còn lại: {self._balance:,.0f} VND"
            )

    # Phương thức lấy số dư
    def get_balance(self):
        return self._balance


# ==========================================
# CHẠY THỬ NGHIỆM
# ==========================================

# 1. Khởi tạo tài khoản
acc = BankAccount("Vu", 5000000)

# 2. Kiểm tra số dư ban đầu
print(f"Số dư ban đầu: {acc.get_balance():,.0f} VND")

# 3. Nạp tiền
acc.deposit(2000000)

# 4. Rút tiền hợp lệ
acc.withdraw(1500000)

# 5. Rút tiền quá số dư (Test chặn lỗi)
acc.withdraw(10000000)
