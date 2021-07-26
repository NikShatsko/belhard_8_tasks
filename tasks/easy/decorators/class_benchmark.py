"""
Написать декоратор, который будет проводить бенчмарк всех методов класса.

До выполнения метода будет печатать:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода будет печатать:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time


def benchmark_decorator(func):
    start_time = time.time()
    end_time = time.time()

    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}\nВремя начала: {start_time}")
        result = func(*args, **kwargs)
        print(
            f"Выполнено {func.__name__}\nВремя окончания: {end_time}\n"
            f"Всего затрачено времени на выполнение: {end_time - start_time}"
        )
        return result

    return wrapper


@benchmark_decorator
class Circle:
    pi: float
    r: float

    def __init__(self, pi: float, r: float):
        self.pi = pi
        self.r = r

    def get_perimeter(self):
        perimeter = 2 * self.pi * self.r
        return perimeter


circle = Circle(3.14, 3)
print(circle.get_perimeter())
