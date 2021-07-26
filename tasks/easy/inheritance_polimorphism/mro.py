"""
Описать класс Cars. Реализовать метод print_fuel_type, который будет генерировать
raise NotImplementedError

Описать класс PetrolMotorCars, который наследуется от Cars. Реализовать метод
print_fuel_type, который будет печатать "Бензин"

Описать класс ElectricMotorCars, который наследуется от Cars. Реализовать метод
print_fuel_type, который будет печатать "Электричество"

Описать класс HybridCars, который наследуется от PetrolMotorCars и ElectricMotorCars
Реализовать метод print_fuel_type, который будет печатать "Бензин + электричество"


Создать объект класса HybridCars. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Cars:
    wheels: int

    def __init__(self, wheels: int):
        self.wheels = wheels

    def print_fuel_type(self):
        raise NotImplementedError


class PetrolMotorCars(Cars):
    cylinders: int

    def __init__(self, wheels: int, cylinders: int):
        super(PetrolMotorCars, self).__init__(wheels)
        self.cylinders = cylinders

    def print_fuel_type(self):
        print("Бензин")


class ElectricMotorCars(Cars):
    electricity: str

    def __init__(self, wheels: int, electricity: str):
        super(ElectricMotorCars, self).__init__(wheels)
        self.electricity = electricity

    def print_fuel_type(self):
        print("Электричество")


class HybridCars(PetrolMotorCars, ElectricMotorCars):
    soul: str

    def __init__(self, wheels: int, cylinders: int, electricity: str, soul: str):
        super(HybridCars, self).__init__(wheels, cylinders, electricity)
        self.soul = soul

    def print_fuel_type(self):
        print("Бензин + электричество")


hybrid = HybridCars(4, 8, "Bzzz", "Jew")
hybrid.print_fuel_type()
print(hybrid.soul())

print(HybridCars.mro())

electro = ElectricMotorCars(4, 'Wzzz')
print(electro.electricity)
moto = PetrolMotorCars(4, 16)
print(moto.wheels)