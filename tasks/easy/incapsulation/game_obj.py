"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- x int
- y int

Координаты должны быть доступны для чтения, а их изменение должно происходить в методе
move(delta_x, delta_y)

реализовать через property
"""


class GameObject:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def move(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def get_coords(self):
        return self.__x, self.__y


game_obj = GameObject()
game_obj.move(10, 20)
print(game_obj.get_coords)






# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # устанавливаем имя
#         self.__age = age  # устанавливаем возраст
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print("Имя:", self.__name, "\tВозраст:", self.__age)
#
#
# tom = Person("Tom", 10)
#
# tom.display_info()
