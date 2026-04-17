# =========================================
# ! BASE CLASS - VEHICLE
# Khung chung cho mọi phương tiện
# =========================================
class Vehicle:
    def __init__(self, brand, speed):
        # * STEP 1: Lưu thông tin cơ bản
        self.brand = brand
        self.speed = speed

    # ! ABSTRACT-LIKE METHOD (nên override)
    def move(self):
        """
        FLOW:
        1. Đây là hành vi chung nhưng KHÔNG đủ cụ thể
        2. Class con nên override để định nghĩa cách di chuyển thực tế
        """
        raise NotImplementedError("Subclass phải override phương thức move()")

    def get_info(self):
        # * STEP 2: Hiển thị thông tin chung
        print(f"Hãng xe: {self.brand} | Tốc độ: {self.speed} Km/h")


# =========================================
# ? CAR (XE HƠI)
# =========================================
class Car(Vehicle):
    def __init__(self, brand, speed, number_of_doors):
        super().__init__(brand, speed)
        self.number_of_doors = number_of_doors

    def move(self):
        # * STEP 3: Hành vi riêng của xe hơi
        print("Xe hơi đang chạy trên đường")


# =========================================
# ? PLANE (MÁY BAY)
# =========================================
class Plane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude

    def move(self):
        # * STEP 4: Hành vi riêng của máy bay
        print("Máy bay đang bay trên trời")


# =========================================
# ? BOAT (THUYỀN)
# =========================================
class Boat(Vehicle):
    def __init__(self, brand, speed, water_type):
        super().__init__(brand, speed)
        self.water_type = water_type

    def move(self):
        # * STEP 5: Hành vi riêng của thuyền
        print("Thuyền đang di chuyển trên nước")


# =========================================
# ! MAIN FLOW - POLYMORPHISM
# =========================================
vehicles = [
    Car("Toyota", 80, 4),
    Plane("Boeing", 900, 10000),
    Boat("Yamaha", 40, "nước ngọt"),
]

"""
FLOW CHẠY:

STEP A: Tạo danh sách các object khác loại nhưng cùng interface (Vehicle)
STEP B: Lặp qua danh sách
STEP C: Gọi cùng 1 method move()
STEP D: Python tự chọn method phù hợp (dynamic dispatch)

→ Đây chính là polymorphism
"""

for v in vehicles:
    v.move()
