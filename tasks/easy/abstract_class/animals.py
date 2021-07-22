"""
Описать абстрактный класс Animal со следующими атрибутами:

- name - кличка
- a_type - домашнее или дикое

и абстрактным методом says()

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод says,
чтобы он выводил, например "Кошка {name} говорит МЯУ"
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    name: str
    a_type: str

    def __init__(self, name: str, a_type: str):
        self.name = name
        self.a_type = a_type

    @abstractmethod
    def says(self):
        pass


class Cat(Animal):
    def __init__(self, name: str, a_type: str):
        super(Cat, self).__init__(name, a_type)

    def says(self):
        print(f"Кошка {self.name} говорит МЯУ")


cat = Cat("Barsik", "home")

cat.says()


class Dog(Animal):
    def __init__(self, name: str, a_type: str):
        super(Dog, self).__init__(name, a_type)

    def says(self):
        print(f"Пес {self.name} {self.a_type}")


dog = Dog("Tuzik", "homeless")
dog.says()


class Cow(Animal):
    def __init__(self, name: str, a_type: str):
        super(Cow, self).__init__(name, a_type)

    def says(self):
        print(f"Корова {self.name} поёт")


cow = Cow("Мурка", "Домашняя")
cow.says()