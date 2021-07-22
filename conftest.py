"""
Наследование
"""
# class Animal:
#     color: str
#     weight: int
#
#     def __init__(self, color: str, weight: int):
#         self.color = color
#         self.weight = weight
#
#
# class Dog(Animal):
#     teeth: int
#
#     def __init__(self, color: str, weight: int, teeth: int):
#         super().__init__(color, weight)
#         self.teeth = teeth
#
#
# dog = Dog("grey", 15, 30)
# print(dog.teeth)
#
#
# class A:
#     def say_a(self):
#         print("a")
#
#
# class B(A):
#     def say_b(self):
#         print("b")
#
#
# class C(A):
#     def say_b(self):
#         print("csads")
#
# class D(B, C):
#     pass
#
#
# d = D()
# d.say_b()

"""
Полиморфизм
"""
# class A:
#     def say(self):
#         print("say a")
#
#
# class B(A):
#     def say(self):
#         super().say()
#         print("say b")
#
# a = A()
# a.say()
# b = B()
# b.say()

"""
Утиная типизация
"""
class A:
    def say(self):
        print("say a")


class B(A):
    def say(self):
        print("say b")


def i_can_say(some_obj):
    some_obj.say()


if __name__ == "__main__":
    a = A()
    b = B()
    i_can_say(a)
    i_can_say(b)


"""Абстрактный класс"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def say(self):
        pass

class Dog(Animal):
    def say(self):
        print('wof')

dog = Dog()
dog.say()

def i_can_say(animal: Animal):
    animal.say()

i_can_say(dog)

"""
Искажение имен
"""
class Cat:
    name: str = "Aboba"
    _weight: int = 10
    __color: str = "Red"

    @property
    def weight(self):
        return f"Вес его {self._weight}"

    @weight.setter
    def weight(self, value):
        self._weight = value()

cat = Cat()
print(cat.name)
print(cat.weight)
print(cat._weight)
print(cat._Cat__color)

cat._weight = 30
print(cat._weight)


"""Метаклассы"""

def print_class_name(some_class):
    print(some_class.__name__)

print_class_name(A)

Dog = type("Dog", tuple(), {
    "color": "grey"
})

print(Dog)
d = Dog()
print(d.color)