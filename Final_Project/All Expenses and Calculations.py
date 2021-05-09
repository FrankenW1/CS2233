from Calculate_Taxes import *
from Assets import *
from Required_Expenses import *

def calc_expenses(costt)

def amount_left(expenses, assets):

if __name__ == '__main__':
    income = int(input('Please Enter Income'))
    state = input('Please Enter State')
    Invest = int(input('Please enter investment'))
    Curr = int(input('Please enter amount currently invested'))
# --------ENDPOINTS FOR TESTING------------
income2 = 48516
Car = 563
Mortgage = 1100
Grocery = 387
Retirement = (income2 / 12) * 0.1
# -----------------------------------------

# ---------ASSETS------------
Investments = Assets(percent_yield=0.1, cost = Invest, currently_invested= Curr)

# ---------------------------

# ---------EXPENSES----------
list_of_expenses = []


Car_Payment = Expenses(cost = Car)
Mortgage = Expenses(cost = 1100)
Groceries = Expenses(cost = Grocery)
k401 = Expenses(cost = Retirement)

for name in Expenses:
    list_of_expenses.append(name)
# ---------------------------

Additional_income_invest = Investments.calculate_additional_income()

