
from tomato_bush import TomatoBush


class Gardener:

    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        print('Садовник работает...')
        self.plants.grow_all()
        print('Садовник закончил')

    def harvest(self):
        print('Садовник собирает урожай...')
        if self.plants.all_are_ripe():
            self.plants.give_away_all()
            print('Садовник закончил')
        else:
            print('Томаты не созрели')


if __name__ == '__main__':
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Садовник', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()
