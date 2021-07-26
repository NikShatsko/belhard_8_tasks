"""
Написать логгирующий декоратор, который все методы класса будет логгировать, т.е.
до выполнения функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__}"
"""


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        return result

    return wrapper


@log_decorator
class Decorator:
    some_args: list
    some_kwargs: dict

    def __init__(self, some_args: list, some_kwargs: dict):
        self.some_args = some_args
        self.some_kwargs = some_kwargs

    def say_hi(self):
        print(f"Say {self.some_args} to {self.some_kwargs}")


decor = Decorator(['a', 'b', 'c'], {"abc": 100, "def": 200})
decor.say_hi()
