class House:
    address: str
    area: float
    cost: int

    def __init__(self, address: str, area: float, cost: int):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, money):
        self.cost += money

    def decrease_cost(self, money):
        self.cost -= money


house1 = House("Street", 60, 1000)
house1.increase_cost(100)
print(house1.cost)
