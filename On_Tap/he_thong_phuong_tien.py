class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print("Phương tiện đang di chuyển")

    def get_info(self):
        print(f"Hãng xe: {self.brand} | Tốc độ: {self.speed} Km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, number_of_doors):
        super().__init__(brand, speed)
        self.number_of_doors = number_of_doors

    def move(self):
        super().move()
        print("Xe hơi đang chạy trên đường")


class Plane(Vehicle):
    def __init__(self, brand, speed, altitude):
        super().__init__(brand, speed)
        self.altitude = altitude

    def move(self):
        super().move()
        print("Máy bay đang bay trên trời")


class Boat(Vehicle):
    def __init__(self, brand, speed, water_type):
        super().__init__(brand, speed)
        self.water_type = water_type

    def move(self):
        super().move()
        print("Thuyền đang di chuyển trên nước")


vehicles = [
    Car("Toyota", 80, 4),
    Plane("Boeing", 900, 10000),
    Boat("Yamaha", 40, "nước ngọt"),
]
for v in vehicles:
    v.move()
