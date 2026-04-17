# =========================================
# ! BASE CLASS - BANK ACCOUNT
# =========================================
class BankAccount:
    def __init__(self, owner, balance):
        # * STEP 1: Khởi tạo
        self._owner = owner

        if balance < 0:
            raise ValueError("Số dư không được < 0")

        self._balance = balance

    # =========================================
    # * DEPOSIT FLOW
    # =========================================
    def deposit(self, amount):
        # STEP 2: Validate
        if amount <= 0:
            raise ValueError("Số tiền nạp phải > 0")

        # STEP 3: Cập nhật
        self._balance += amount

        print(f"[{self._owner}] +{amount:,.0f} | {self._balance:,.0f}")

    # =========================================
    # * WITHDRAW FLOW (DEFAULT)
    # =========================================
    def withdraw(self, amount):
        """
        FLOW:
        1. Validate input
        2. Kiểm tra đủ tiền
        3. Trừ tiền
        """

        # STEP 4
        if amount <= 0:
            raise ValueError("Số tiền rút phải > 0")

        # STEP 5
        if amount > self._balance:
            raise ValueError("Không đủ tiền")

        # STEP 6
        self._balance -= amount

        print(f"[{self._owner}] -{amount:,.0f} | {self._balance:,.0f}")

    def get_balance(self):
        return self._balance


# =========================================
# ? SAVINGS ACCOUNT
# =========================================
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        if interest_rate < 0:
            raise ValueError("Lãi suất không hợp lệ")

        self.interest_rate = interest_rate

    def add_interest(self):
        """
        FLOW:
        1. Tính lãi
        2. Cộng vào số dư
        """

        interest = self._balance * self.interest_rate / 100
        self._balance += interest

        print(f"[{self._owner}] +Lãi: {interest:,.0f}")


# =========================================
# ? CHECKING ACCOUNT (OVERDRAFT)
# =========================================
class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = -500

    def withdraw(self, amount):
        """
        FLOW:
        1. Validate input
        2. Tính số dư mới
        3. Kiểm tra limit âm
        4. Cập nhật
        """

        if amount <= 0:
            raise ValueError("Số tiền không hợp lệ")

        # STEP 7
        new_balance = self._balance - amount

        # STEP 8
        if new_balance < self.OVERDRAFT_LIMIT:
            raise ValueError("Vượt hạn mức thấu chi")

        # STEP 9
        self._balance = new_balance

        print(f"[{self._owner}] -{amount:,.0f} | {self._balance:,.0f}")


# =========================================
# ! TEST FLOW
# =========================================
acc = CheckingAccount("An", 1000)

# STEP A: Rút hợp lệ
acc.withdraw(1300)  # → -300

# STEP B: Vượt limit
try:
    acc.withdraw(300)
except ValueError as e:
    print("❌", e)
