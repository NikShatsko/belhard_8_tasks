"""
Описать класс Shape - фигура, у которого должно быть 2 абстрактных метода:
- get_perimeter для расчета периметра
- get_square для расчета площади

Описать класс Circle для круга, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Длина окружности = 2 * pi * r
Площадь = pi * r ** 2

Описать класс Rectangle для прямоугольника, отнаследоваться от фигуры
добавить недостающие атрибуты
перегрузить методы get_perimeter и get_square
Периметр = 2 * a + 2 * b
Площадь = a * b


Описать класс Square для квадрата, отнаследоваться от прямоугольника
перегрузить методы get_perimeter и get_square
Периметр = 4 * a
Площадь = a ** 2
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):
    pi: float
    r: float

    def __init__(self, pi: float, r: float):
        super(Circle, self).__init__()
        self.pi = pi
        self.r = r

    def get_perimeter(self):
        perimeter = 2 * self.pi * self.r
        return perimeter

    def get_square(self):
        square = self.pi * self.r ** 2
        return square


circle = Circle(3.14, 3)
print("Circle")
print(circle.get_square())
print(circle.get_perimeter())


class Rectangle(Shape):
    a: int
    b: int

    def __init__(self, a: int, b: int):
        super(Rectangle, self).__init__()
        self.a = a
        self.b = b

    def get_perimeter(self):
        perimeter = 2 * self.a + 2 * self.b
        return perimeter

    def get_square(self):
        square = self.a * self.b
        return square


rectangle = Rectangle(6, 8)
print("Rectangle")
print(rectangle.get_perimeter())
print(rectangle.get_square())


class Square(Rectangle):
    def __init__(self, a: int, b: int):
        super(Square, self).__init__(a, b)

    def get_perimeter(self):
        perimeter = self.a * 4
        return perimeter

    def get_square(self):
        square = self.a ** 2
        return square


square = Square(5, 5)
print("Square")
print(square.get_square())
print(square.get_perimeter())
