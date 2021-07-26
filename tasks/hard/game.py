"""
Создать класс Warrior

Определить атрибуты:

- name - имя юнита
- health_points - int от 0 до 100

Определить методы:

- инициализатор __init__, который создает юнита со 100 health_points
- метод hit, который реализует удар, от которого снимается 20 health_points
  у другого юнита

Создать список, в который добавить 5 объектов класса Warrior.

В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
У того, кого бьют, оно уменьшается на 20 очков от одного удара.
После каждого удара надо выводить сообщение, какой юнит атаковал,
и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья он удаляется из списка.
Программа завершается, когда останется один юнит, на экран выводится сообщение о том,
кто одержал победу.
"""
import random


class Warrior:
    def __init__(self, health):
        self.health = health

    def hit(self, target, target1):
        if target.health > 0:
            target.health -= 20
            if target1 == warrior1:
                target1 = "Warrior1"
            if target1 == warrior2:
                target1 = "Warrior2"
            print(target1, " has attacked")
            print(target.health, " left")
        if target.health == 0:
            print(target1, " has won")


warrior1 = Warrior(100)
warrior2 = Warrior(100)

q = int(input("Enter 1 to let some warrior attack. Enter 2 to stop program:"))

while q != 2:
    if q == 1:
        j = random.randint(1, 3)
        if j % 2 == 0:
            warrior1.hit(warrior2, warrior1)
            q = int(input("Enter 1 to let some warrior attack:"))
        else:
            warrior2.hit(warrior1, warrior2)
            q = int(input("Enter 1 to let some warrior attack:"))
    else:
        print("Wrong input.")
        break
