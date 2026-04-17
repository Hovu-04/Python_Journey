# =========================================
# ! ACCOUNT - BASE CLASS
# Quản lý số dư + nạp/rút tiền
# =========================================
class Account:
    def __init__(self, owner, balance):
        # * STEP 1: Gán thông tin chủ tài khoản
        self.owner = owner

        # * STEP 2: Gán số dư qua setter → validate ngay từ đầu
        self.balance = balance

    # =========================================
    # * BALANCE FLOW (ENCAPSULATION)
    # =========================================
    @property
    def balance(self):
        # * STEP 3: Trả về số dư hiện tại
        return self._balance

    @balance.setter
    def balance(self, value):
        # * STEP 4: Rule dữ liệu (không cho âm)
        if value < 0:
            raise ValueError("Số tiền không được là số âm!")
        self._balance = value

    # =========================================
    # ! BUSINESS FLOW: RÚT TIỀN
    # =========================================
    def withdraw(self, amount):
        """
        FLOW:
        1. Validate số tiền rút
        2. Tính số dư mới
        3. Kiểm tra đủ tiền
        4. Cập nhật qua setter
        """

        # * STEP 5: Validate input
        if amount <= 0:
            raise ValueError("Số tiền rút phải > 0")

        print(f"Số dư hiện tại: {self.balance:,} VND")

        # * STEP 6: Tính số dư mới
        new_balance = self.balance - amount

        # * STEP 7: Rule nghiệp vụ (không được âm)
        if new_balance < 0:
            raise ValueError("Không đủ tiền để rút")

        # * STEP 8: Gán qua setter
        self.balance = new_balance

        print(f"Đã rút {amount:,} VND | Còn: {self.balance:,} VND")

    # =========================================
    # ! BUSINESS FLOW: NẠP TIỀN
    # =========================================
    def recharge(self, amount):
        """
        FLOW:
        1. Validate số tiền nạp
        2. Cộng vào số dư
        3. Gán qua setter
        """

        # * STEP 9: Validate input
        if amount <= 0:
            raise ValueError("Số tiền nạp phải > 0")

        # * STEP 10: Cập nhật
        self.balance = self.balance + amount

        print(f"Đã nạp {amount:,} VND | Số dư: {self.balance:,} VND")


# =========================================
# ? SAVINGS ACCOUNT (TÍNH LÃI)
# =========================================
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_monthly_interest(self):
        """
        FLOW:
        1. Tính tiền lãi
        2. Cộng vào số dư
        """

        # * STEP 11: Tính lãi
        interest = self.balance * self.interest_rate / 100

        # * STEP 12: Cộng lãi
        self.balance = self.balance + interest

        print(f"+Lãi: {interest:,.0f} VND ({self.interest_rate}%/tháng)")


# =========================================
# ? CHECKING ACCOUNT (CÓ PHÍ RÚT)
# =========================================
class CheckingAccount(Account):
    def __init__(self, owner, balance, withdrawal_fee):
        super().__init__(owner, balance)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, amount):
        """
        FLOW:
        1. Nhận số tiền muốn rút
        2. Cộng thêm phí
        3. Gọi logic rút tiền của class cha
        """

        # * STEP 13: Tính tổng tiền bị trừ
        total_withdraw = amount + self.withdrawal_fee

        print(f"Phí: {self.withdrawal_fee:,} | Tổng trừ: {total_withdraw:,} VND")

        # * STEP 14: Delegate cho class cha xử lý
        super().withdraw(total_withdraw)


# =========================================
# ! TEST FLOW
# =========================================

# STEP A: Tạo tài khoản tiết kiệm
savings_acc = SavingsAccount("Bạn", 10_000_000, 0.5)

# STEP B: Nạp tiền
savings_acc.recharge(2_000_000)

# STEP C: Cộng lãi
savings_acc.add_monthly_interest()

print("\n--- Checking ---")

# STEP D: Tạo tài khoản thanh toán
checking_acc = CheckingAccount("Bạn", 5_000_000, 5_000)

# STEP E: Rút tiền (có phí)
checking_acc.withdraw(1_000_000)
