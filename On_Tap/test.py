# Lớp cha giữ nguyên như cũ
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        if balance < 0:
            raise ValueError("Số dư tài khoản không đươc nhỏ hơn 0!")
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền nạp phải lớn hơn 0!")
        self._balance += amount
        print(
            f"[{self._owner}] Nạp thành công: {amount:,.0f} VND | Số dư mới: {self._balance:,.0f} VND"
        )

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

    # Phương thức xử lý cuối tháng - lớp cha định nghĩa giao diện chung
    def monthly_process(self):
        print(f"[{self._owner}] Hoàn thành xử lý cuối tháng cho tài khoản cơ bản!")

    def get_balance(self):
        return self._balance


# Lớp con SavingsAccount - ghi đè monthly_process
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        if interest_rate < 0:
            raise ValueError("Lãi xuất không được nhỏ hơn 0!")
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate / 100
        self._balance += interest
        print(
            f"[{self._owner}] Đã cộng lãi suất ({self.interest_rate}%): +{interest:,.0f} VND"
        )
        print(f"Số dư mới sau khi cộng lãi: {self._balance:,.0f} VND")

    # Ghi đè phương thức xử lý cuối tháng riêng cho tiết kiệm
    def monthly_process(self):
        print(f"[{self._owner}] Bắt đầu xử lý cuối tháng cho tài khoản tiết kiệm...")
        self.add_interest()


# Lớp con CheckingAccount - cũng ghi đè monthly_process
class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = -500

    def __init__(self, owner, balance):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền cần rút không được nhỏ hơn 0!")
        if self._balance - amount < self.OVERDRAFT_LIMIT:
            print(
                f"Thất bại! Số dư không được xuống dưới {self.OVERDRAFT_LIMIT:,.0f} VND"
            )
        self._balance -= amount
        print(
            f"[{self._owner}] Rút thành công: {amount:,.0f} VND | Số dư mới: {self._balance:,.0f} VND"
        )

    # Ghi đè phương thức xử lý cuối tháng riêng cho thanh toán
    def monthly_process(self):
        print(f"[{self._owner}] Bắt đầu xử lý cuối tháng cho tài khoản thanh toán...")
        if self._balance < 0:
            print(
                f"⚠️ Cảnh báo: Tài khoản đang thấu chi {abs(self._balance):,.0f} VND, vui lòng nạp tiền trong 7 ngày!"
            )
        else:
            print(f"✅ Tài khoản thanh toán trạng thái bình thường!")


accounts = [
    SavingsAccount("Vũ", 1000, 5),
    CheckingAccount("An", 500),
]

for acc in accounts:
    acc.monthly_process()
