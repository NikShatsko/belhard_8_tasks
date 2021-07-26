"""
Описать логгирующий метакласс, который все методы класса будет логгировать, т.е.
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


class SomeMeta(type):
    def __new__(mcs, name, bases, attr, **extra_kwargs):
        new_class = super().__new__(name, bases, attr, **extra_kwargs)
        functions = {k: v for k, v in new_class.__dict__.items() if callable(v)}
        for k, v in functions.items():
            func_with_dec = decor(v)
            setattr(new_class, k, func_with_dec)
