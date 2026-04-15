class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @owner.setter
    def owner(self, value):
        if not value:
            raise ValueError("Không để trống tên chủ tài khoản")
        self._owner = value

    def balance(self, value):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass


b = BankAccount("Vu", 3000000)
b.owner = "Hao"
print(b.owner)
