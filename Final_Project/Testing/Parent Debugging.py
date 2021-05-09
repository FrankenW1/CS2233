class Expenses:
    def __init__(self, cost = 0, name: str = ''):
        self.cost = cost
        self.name = name



class Assets(Expenses):
    def __init__(self, income, cost, name):
        super().__init__(cost, name)
        self.income = income


B = Assets(110000, 150, 'death')
print(B.cost)
