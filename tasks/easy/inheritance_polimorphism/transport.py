"""
Описать класс Transport, у которого следующие атрибуты:

- brand - фирма, выпустившая транспорт
- model - модель
- issue_year - год выпуска
- color - цвет

Определить методы:

- move - который делает raise NotImplementedError

Описать класс Car, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- engine_type

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} проехала {km} километров"

Описать класс Airplane, который наследуется от Transport, у которого следующие атрибуты:

- mileage - пробег
- lifting_capacity - грузоподъемность

Определить методы:

- move - который принимает количество километров, увеличивает на это количество пробег
  и печатает "{brand} {model} пролетел {km} километров"
"""


class Transport:
    brand: str
    model: str
    issue_year: int
    color: str

    def __init__(self, brand: str, model: str, issue_year: int, color: str):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.color = color

    def move(self):
        raise NotImplementedError


class Car(Transport):
    mileage: int
    engine_type: str

    def __init__(self, brand: str, model: str, issue_year: int, color: str, mileage: int, engine_type: str):
        super(Car, self).__init__(brand, model, issue_year, color)
        self.mileage = mileage
        self.engine_type = engine_type

    def move(self, distance):
        print(f"{self.brand} {self.model} проехала {self.mileage} километров")
        self.mileage += distance


class Airplane(Transport):
    mileage: int
    lifting_capacity: int

    def __init__(self, brand: str, model: str, issue_year: int, color: str, mileage: int, lifting_capacity: int):
        super(Airplane, self).__init__(brand, model, issue_year, color)
        self.mileage = mileage
        self.lifting_capacity = lifting_capacity

    def move(self, distance):
        print(f"{self.brand} {self.model} пролетел {self.mileage} километров")
        self.mileage += distance


airplane = Airplane("Boing", "a-800", 2008, "Red", 1000000, 5000)
airplane.move(1000)
print(airplane.mileage)