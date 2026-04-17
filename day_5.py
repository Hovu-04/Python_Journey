# =========================================
# ! BASE CLASS - BANK ACCOUNT
# Quản lý hành vi chung: nạp, rút, xử lý cuối tháng
# =========================================
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner

        # * STEP 1: Validate số dư ban đầu
        if balance < 0:
            raise ValueError("Số dư tài khoản không được nhỏ hơn 0!")

        self._balance = balance

    # =========================================
    # * FLOW: NẠP TIỀN
    # =========================================
    def deposit(self, amount):
        # STEP 2: Validate input
        if amount <= 0:
            raise ValueError("Số tiền nạp phải lớn hơn 0!")

        # STEP 3: Cộng tiền
        self._balance += amount

        print(f"[{self._owner}] +{amount:,.0f} | Số dư: {self._balance:,.0f}")

    # =========================================
    # * FLOW: RÚT TIỀN (mặc định)
    # =========================================
    def withdraw(self, amount):
        # STEP 4: Validate input
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0!")

        # STEP 5: Kiểm tra đủ tiền
        if amount > self._balance:
            print(f"[{self._owner}] ❌ Không đủ tiền")
            return

        # STEP 6: Trừ tiền
        self._balance -= amount

        print(f"[{self._owner}] -{amount:,.0f} | Còn: {self._balance:,.0f}")

    # =========================================
    # ! TEMPLATE METHOD: xử lý cuối tháng
    # =========================================
    def monthly_process(self):
        # STEP 7: Logic mặc định (có thể bị override)
        print(f"[{self._owner}] Xử lý cuối tháng (mặc định)")

    def get_balance(self):
        return f"[{self._owner}] | Số dư: {self._balance:,.0f}"


# =========================================
# ? SAVINGS ACCOUNT (có lãi)
# =========================================
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        if interest_rate < 0:
            raise ValueError("Lãi suất không được nhỏ hơn 0!")

        self.interest_rate = interest_rate

    def add_interest(self):
        # STEP 8: Tính lãi
        interest = self._balance * self.interest_rate / 100

        # STEP 9: Cộng lãi
        self._balance += interest

        print(f"[{self._owner}] +Lãi: {interest:,.0f}")

    # ! Override monthly_process
    def monthly_process(self):
        """
        FLOW:
        1. Bắt đầu xử lý cuối tháng
        2. Tính lãi
        """
        print(f"[{self._owner}] 🔄 Xử lý tài khoản tiết kiệm")
        self.add_interest()


# =========================================
# ? CHECKING ACCOUNT (cho phép thấu chi)
# =========================================
class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = -500

    def withdraw(self, amount):
        # STEP 10: Validate input
        if amount <= 0:
            raise ValueError("Số tiền không hợp lệ")

        new_balance = self._balance - amount

        # ! STEP 11: Kiểm tra hạn mức thấu chi
        if new_balance < self.OVERDRAFT_LIMIT:
            print(f"[{self._owner}] ❌ Vượt hạn mức thấu chi")
            return  # 🔥 FIX QUAN TRỌNG (tránh trừ tiền tiếp)

        # STEP 12: Trừ tiền
        self._balance = new_balance

        print(f"[{self._owner}] -{amount:,.0f} | Số dư: {self._balance:,.0f}")

    # ! Override monthly_process
    def monthly_process(self):
        """
        FLOW:
        1. Kiểm tra trạng thái tài khoản
        2. Nếu âm → cảnh báo
        """
        print(f"[{self._owner}] 🔄 Xử lý tài khoản thanh toán")

        if self._balance < 0:
            print(f"⚠️ Thấu chi {abs(self._balance):,.0f}")
        else:
            print("✅ Trạng thái bình thường")


# =========================================
# ! MAIN FLOW (POLYMORPHISM)
# =========================================
accounts = [
    SavingsAccount("Vũ", 100000, 5),
    CheckingAccount("An", 50000),
]

for acc in accounts:
    # STEP A: Gọi cùng 1 method → hành vi khác nhau (polymorphism)
    acc.withdraw(30000)

    # STEP B: Xử lý cuối tháng theo từng loại tài khoản
    acc.monthly_process()
