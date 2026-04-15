class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Số tiền không được là số âm!")
        self._balance = value

    def withdraw(self, amount):
        print(f"Số dư hiện tại: {self.balance:,} VND")
        self.balance = self.balance - amount
        print(f"Đã rút thành công {amount:,} VND. Số dư mới: {self.balance:,} VND")

    def recharge(self, amount):
        if amount <= 0:
            print(f"❌ Lỗi: Số tiền nạp ({amount:,}) phải lớn hơn 0!")
            return
        self.balance = self.balance + amount
        print(f"✅ Đã nạp thành công {amount:,} VND. Số dư mới: {self.balance:,} VND")


# --- LỚP CON 1: Tài khoản tiết kiệm ---
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        # Gọi hàm khởi tạo của lớp cha để lấy owner, balance
        super().__init__(owner, balance)
        # Thêm thuộc tính riêng: lãi suất %/tháng
        self.interest_rate = interest_rate

    # Phương thức riêng: tính lãi hàng tháng
    def add_monthly_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance = self.balance + interest
        print(f"✅ Đã cộng lãi {interest:,} VND (lãi suất {self.interest_rate}%/tháng)")


# --- LỚP CON 2: Tài khoản thanh toán ---
class CheckingAccount(Account):
    def __init__(self, owner, balance, withdrawal_fee):
        super().__init__(owner, balance)
        # Thêm thuộc tính riêng: phí rút tiền mỗi giao dịch
        self.withdrawal_fee = withdrawal_fee

    # Ghi đè phương thức withdraw của lớp cha (thêm phí)
    def withdraw(self, amount):
        total_withdraw = amount + self.withdrawal_fee
        print(
            f"Phí rút tiền: {self.withdrawal_fee:,} VND. Tổng trừ: {total_withdraw:,} VND"
        )
        super().withdraw(total_withdraw)


# --- KIỂM TRA CHẠY THỬ ---
print("--- TÀI KHOẢN TIẾT KIỆM ---")
savings_acc = SavingsAccount("Bạn", 10000000, 0.5)  # Lãi 0.5%/tháng
savings_acc.recharge(2000000)  # Nạp thêm 2tr
savings_acc.add_monthly_interest()  # Cộng lãi

print("\n--- TÀI KHOẢN THANH TOÁN ---")
checking_acc = CheckingAccount("Bạn", 5000000, 5000)  # Phí rút 5k
checking_acc.withdraw(1000000)  # Rút 1tr, tổng trừ 1.005.000
