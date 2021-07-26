"""
Создать класс BookCard, в классе должны быть закрытые атрибуты:

- author - автор
- title - название книги
- publishing_house - издательство
- year - год издания
- num_pages - количество страниц
- num_copies - тираж

Определить методы:

- инициализатор __init__
- магические методы сравнения для сортировки книг по году издания

в сеттерах сделать проверки на тип данных. Если тип данных не подходит, то генерировать
ValueError. Для года издания дополнительно проверить на валидность, num_pages и
num_copies должны быть больше 0

реализовать через property
"""


class BookCard:

    def __init__(self, author: str, title: str, publishing_house: str, year: int, num_pages: int,
                 num_copies: int):
        self.__author = author
        self.__title = title
        self.__publishing_house = publishing_house
        self.__year = year
        self.__num_pages = num_pages
        self.__num_copies = num_copies

    def __gt__(self, other):
        return self.__year > other.__year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year_type(self, year):
        if isinstance(self.__year, int):
            self.__year = year
        else:
            raise ValueError

    def number_check(self):
        if self.__num_pages <= 0 or self.__num_copies <= 0:
            raise ValueError
        else:
            pass

    def __repr__(self):
        return f"Автор: {self.__author}, название: {self.__title}, год: {self.__year}\n"


books = [
    BookCard('a', 'a', 'a', 2000, 0, 1000),
    BookCard('b', 'b', 'b', 2002, 200, 500),
    BookCard('c', 'c', 'c', 1995, 300, 1023)
]

print(sorted(books))
