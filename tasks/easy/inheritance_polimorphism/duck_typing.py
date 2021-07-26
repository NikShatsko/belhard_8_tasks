"""
Создать 3 класса:

Cat, Duck, Cow

в каждом классе определить метод says()

Cat.says() - кошка говорит мяу
Duck.says() - утка говорит кря
Cow.says() - корова говорит муу


Написать функцию animal_says(), которая принимает объект и вызывает метод says
"""


class Cat:
    def says(self):
        print("кошка говорит мяу")


class Duck:
    def says(self):
        print("утка говорит кря")


class Cow:
    def says(self):
        print("корова говорит муу")


def animal_says(animal):
    animal.says()


animal_says(Cat())
animal_says(Duck())
animal_says(Cow())

