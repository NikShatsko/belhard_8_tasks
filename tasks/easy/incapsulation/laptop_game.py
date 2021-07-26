"""
Написать класс Laptop (ноутбук), со следующими скрытыми атрибутами:

- cpu_cores - количество ядер процессора
- gpu_total - количество ГБ видеопамяти
- ram_total - количество ГБ ОЗУ

Определить методы:

- инициализатор __init__, с помощью которого присваиваются скрытые атрибуты
- метод can_play(game_name, cpu_cores, gpu_total, ram_total). Если требования игры
  меньше, чем характеристики компьютера, то вывести
  "На данном ПК есть возможность играть в {game_name}"
"""


class Laptop:
    def __init__(self, cpu_cores, gpu_total, ram_total):
        self.__cpu_cores = cpu_cores
        self.__gpu_total = gpu_total
        self.__ram_total = ram_total

    def can_play(self, game_name, cpu_cores, gpu_total, ram_total):
        if self.__cpu_cores >= cpu_cores and self.__gpu_total >= gpu_total and self.__ram_total >= ram_total:
            print(f"На данном ПК есть возможность играть в {game_name}")
        else:
            print(f"Данный ПК не потянет {game_name}")


laptop = Laptop(4, 6, 8)
laptop.cpu_cores = 12
laptop.can_play("DOOM", 8, 4, 6)


# class Laptop:
#     def __init__(self, cpu_cores, gpu_total, ram_total):
#         self.cpu_cores = cpu_cores
#         self.gpu_total = gpu_total
#         self.ram_total = ram_total
#
#     def can_play(self, game_name, cpu_cores, gpu_total, ram_total):
#         if self.cpu_cores >= cpu_cores and self.gpu_total >= gpu_total and self.ram_total >= ram_total:
#             print(f"На данном ПК есть возможность играть в {game_name}")
#         else:
#             print(f"Данный ПК не потянет {game_name}")
#
#
# laptop = Laptop(4, 6, 8)
# laptop.cpu_cores = 12
# laptop.can_play("DOOM", 8, 4, 6)