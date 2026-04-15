class Test:
    def __init__(self):
        self.value = 10  # gọi setter

    @property
    def value(self):
        print("GETTER chạy")
        return self._value

    @value.setter
    def value(self, v):
        print("SETTER chạy")
        self._value = v


t = Test()
print(t.value)
