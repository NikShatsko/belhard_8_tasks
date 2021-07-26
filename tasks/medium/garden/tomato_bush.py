from tomato import Tomato


class TomatoBush:
    tomato_list: list

    def __init__(self, num):
        self.tomato_list = [Tomato(index) for index in range(0, num - 1)]

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomato_list])

    def give_away_all(self):
        self.tomato_list = []
