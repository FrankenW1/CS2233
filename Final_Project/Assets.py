from Required_Expenses import Expenses

class Assets(Expenses):
    def __init__(self, percent_yield, cost: int = 0, currently_invested: float = 0.0):
        super().__init__(cost)
        self.percent_yield = percent_yield / 12
        self.invested = currently_invested
    def calculate_additional_income(self):
        self.additional_income = (self.cost + self.invested) * self.percent_yield
        return self.additional_income


