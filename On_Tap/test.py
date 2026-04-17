from abc import ABC, abstractmethod


class IdolGioiTre(ABC):
    def __init__(self, name, age, appearance):
        self.name = name
        self.age = age
        self.__appearance = appearance

    def get_appearance(self):
        return self.__appearance

    def set_appearance(self, value):
        if not value:
            raise ValueError("Không được rỗng")
        self.__appearance = value

    @abstractmethod
    def live_stream(self):
        pass

    @abstractmethod
    def signature_quote(self):
        pass


class KhaBanh(IdolGioiTre):
    def __init__(self, name, age, appearance, location):
        super().__init__(name, age, appearance)
        self.location = location

    def live_stream(self):
        print("Livestream tại", self.location)

    def signature_quote(self):
        print("Ảo thật đấy!")


class TienBip(IdolGioiTre):
    def live_stream(self):
        print("Livestream chill")

    def signature_quote(self):
        print("Còn cái nịt!")


# Polymorphism
idols = [KhaBanh("Khá", 30, "Đầu moi", "Trong tù"), TienBip("Tiến", 28, "Cool")]

for idol in idols:
    idol.live_stream()
    idol.signature_quote()
