from house import House


class Townhouse(House):
    def __init__(self, address, area, cost):
        super(Townhouse, self).__init__(address, area, cost)
        self.area = 60


townhouse = Townhouse("street", 50, 1000)
print(townhouse.area)
