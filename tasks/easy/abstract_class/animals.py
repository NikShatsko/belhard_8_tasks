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

    @property
    def animal_status(self):
        print(f"{self.name} is {self.a_type}")


class Cat(Animal):
    def __init__(self, name: str, a_type: str):
        super(Cat, self).__init__(name, a_type)

    def says(self):
        print(f"Кошка {self.name} говорит МЯУ")


cat = Cat("Barsik", "home")

cat.says()
cat.animal_status


class Dog(Animal):
    def __init__(self, name: str, a_type: str):
        super(Dog, self).__init__(name, a_type)

    def says(self):
        print(f"Пес {self.name} {self.a_type}")


dog = Dog("Tuzik", "homeless")
dog.says()
dog.animal_status


class Cow(Animal):
    def __init__(self, name: str, a_type: str):
        super(Cow, self).__init__(name, a_type)

    def says(self):
        print(f"Корова {self.name} поёт")


cow = Cow("Мурка", "Домашняя")
cow.says()
cow.animal_status