# =========================================
# ! ACCOUNT - DOMAIN MODEL
# Quản lý số dư với encapsulation qua property
# =========================================
class Account:
    def __init__(self, owner, balance):
        self.owner = owner

        # * Gọi setter ngay từ đầu để validate
        self.balance = balance

    # =========================================
    # * PROPERTY: balance (read-only từ bên ngoài)
    # =========================================
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        # ! Rule cốt lõi: Không cho số dư âm
        if value < 0:
            raise ValueError("Số tiền không được là số âm!")
        self._balance = value

    # =========================================
    # * NẠP TIỀN (business logic)
    # =========================================
    def recharge(self, amount):
        if amount <= 0:
            # ⚠️ Không nên dùng print cho lỗi (chỉ demo)
            print(f"❌ Lỗi: Số tiền nạp ({amount}) phải > 0!")
            return

        # * Update qua setter để reuse validation
        self.balance = self.balance + amount

        print(f"✅ Nạp {amount:,} VND | Số dư: {self.balance:,} VND")

    # =========================================
    # * RÚT TIỀN (business logic)
    # =========================================
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Số tiền rút phải > 0")

        # ! Delegation cho setter kiểm soát âm
        try:
            self.balance = self.balance - amount
        except ValueError:
            # * Convert technical error -> business message
            print(f"❌ Không đủ tiền để rút {amount:,} VND")
            return

        print(f"✅ Rút {amount:,} VND | Còn: {self.balance:,} VND")


# =========================================
# ! TEST FLOW
# =========================================
acc = Account("Bạn", 2_000_000)

# * Case hợp lệ
acc.recharge(500_000)

# * Case vượt số dư
acc.withdraw(2_000_000)
