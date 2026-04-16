class Bicycle:
    def __init__(self, bike_id, bike_type):
        self.bike_id = bike_id
        self.bike_type = bike_type
        self.is_available = True

    def rent(self):
        if not self.is_available:
            raise Exception("Xe đã được thuê")
        self.is_available = False

    def return_bike(self):
        self.is_available = True


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Payment:
    def pay(self, amount):
        raise NotImplementedError


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Thanh toán tiền mặt: {amount}")


class VNPayPayment(Payment):
    def pay(self, amount):
        print(f"Thanh toán qua VNPay: {amount}")


class RentalOrder:
    def __init__(self, customer, payment):
        self.customer = customer
        self.payment = payment
        self.bicycles = []
        self.hours = 0

    def add_bicycle(self, bike):
        if not bike.is_available:
            raise Exception("Xe không khả dụng")
        self.bicycles.append(bike)

    def set_hours(self, hours):
        self.hours = hours

    def calculate_total(self):
        price_per_hour = 10000
        return len(self.bicycles) * self.hours * price_per_hour

    def checkout(self):
        total = self.calculate_total()

        # thuê xe
        for bike in self.bicycles:
            bike.rent()

        # thanh toán (đa hình)
        self.payment.pay(total)

        print("Thuê xe thành công!")


# tạo dữ liệu
bike1 = Bicycle(1, "mountain")
bike2 = Bicycle(2, "road")

customer = Customer("Vũ", "0123456789")

payment = VNPayPayment()  # đổi sang CashPayment cũng được

# tạo đơn thuê
order = RentalOrder(customer, payment)

order.add_bicycle(bike1)
order.add_bicycle(bike2)
order.set_hours(3)

order.checkout()
