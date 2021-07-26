class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        self.change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        else:
            return False

    def change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Помидор {self.index}  {Tomato.states[self.state]}')

# class Tomato:
#     ripeness: str
#     states = ("Отсутствует", "Цветение", "Зеленый", "Красный")
#
#     def __init__(self, index):
#         self.ripeness = self.states[0]
#         self.index = index
