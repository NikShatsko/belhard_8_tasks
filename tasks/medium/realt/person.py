from house import House
from townhouse import Townhouse


class Person:
    name: str
    age: int
    money: int
    realty: list

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        print(f"{self.name}, {self.age}, {self.realty}, {self.money}")

    def earn_money(self, salary):
        self.money += salary

    def make_deal(self, house1, cost):
        if self.money >= house1.cost:
            self.money -= cost
            self.realty.append(house1)
        else:
            print("недостаточно денег")


if __name__ == '__main__':
    house1 = House("Street", 60, 1000)
    house1.increase_cost(100)

    townhouse = Townhouse("street", 50, 1000)

    person = Person("Van", 40)
    person.earn_money(5000)
    print(person.money)
    person.make_deal(house1, 1000)
    print(person.money)
