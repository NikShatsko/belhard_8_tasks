"""
Определить класс Person с атрибутами:

- fio - ФИО
- phone - номер телефона

Описать класс LibraryReader, который наследуется от Person c атрибутами:

- id - номер читательского билета
- books - список книг

Определить методы:

- инициализатор __init__
- take_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. взял книги: Приключения, Словарь, Энциклопедия", если взято до 3 книг, и
  "Петров В. В. взял 4 книги", если больше

- return_book(*args) - принимает произвольное количество книг и выводит сообщение:
  "Петров В. В. вернул книги: Приключения, Словарь, Энциклопедия", если вернул до 3 книг
  и "Петров В. В. вернул 4 книги". Если какой то книги нет, то выводится сообщение
  "Петров В. В. не брал Рассказы"
"""


class Person:
    fio: str
    phone: int

    def __init__(self, fio: str, phone: int):
        self.fio = fio
        self.phone = phone


class LibraryReader(Person):
    id: int
    books: list

    def __init__(self, fio: str, phone: int, id: int, books: list):
        super(LibraryReader, self).__init__(fio, phone)
        self.id = id
        self.books = books

    def take_book(self, *args):
        for some_book in args:
            self.books.append(some_book)
        if len(args) > 3:
            print("Петров В. В. взял 4 книги")
        else:
            print(f"Петров В. В. взял книги: {self.books}")

    def return_books(self, *args):
        for some_book in args:
            self.books.append(some_book)
        if len(args) > 3:
            print("Петров В. В. вернул 4 книги")
        else:
            print(f"Петров В. В. вернул книги: {self.books}")
        # if some_book not in self.books:
        #     print(f"Петров В. В. не брал {self.books}")


petrov = LibraryReader("PEO", 666, 123, ['AAAA', 'Abbb', 'asdasfd', '213123'])
petrov.take_book()
petrov = LibraryReader("PEO", 666, 123, ['AAAA', 'Abbb', 'asdasfd'])
petrov.return_books()
print(petrov.books)
