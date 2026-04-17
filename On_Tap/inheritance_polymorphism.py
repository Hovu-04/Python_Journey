# Inheritance and Polymorphism

class Vehicle:
    def start(self):
        pass

class Bicycle(Vehicle):
    def start(self):
        print("Bicycle started")

# Example Usage
bicycle = Bicycle()
bicycle.start()