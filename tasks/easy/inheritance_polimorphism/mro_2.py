"""
Описать класс Device. Реализовать метод process_doc, который будет генерировать
raise NotImplementedError

Описать класс Scanner, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Сканирую документ: {name}"

Описать класс Copier, который наследуется от Device. Реализовать метод
process_doc, который будет печатать "Делаю копию: {name}"

Описать класс MFU, который наследуется от Scanner и Copier
Реализовать метод process_doc, который будет печатать "Сканирую, отправляю факс: {name}"

Создать объект класса MFU. Потренироваться вызывать методы через super,
через имя класса. Просмотреть MRO
"""


class Device:
    name: str

    def __init__(self, name: int):
        self.name = name

    def process_doc(self):
        raise NotImplementedError


class Scanner(Device):

    def process_doc(self):
        print(f"Сканирую документ: {self.name}")


class Copier(Device):
    num_copie: int

    def __init__(self, name: str, num_copie: int):
        super(Copier, self).__init__(name)
        self.num_copie = num_copie

    def process_doc(self):
        print(f"Делаю копию: {self.name}")


class MFU(Scanner, Copier):
    mfy1: str

    def __init__(self, name: str, num_copie: int, mfy1: str):
        super(MFU, self).__init__(name, num_copie)
        self.mfy1 = mfy1

    def process_doc(self):
        print(f"Сканирую, отправляю факс: {self.name}")


mfu = MFU("Nice", 11, "Wzzz")
mfu.process_doc()
print(mfu.num_copie)
print(MFU.mro())