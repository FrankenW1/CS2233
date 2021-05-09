class StateIncomeTax:
    def __init__(self,name: str, abbreviation: str, tax: float):
        self.name = name
        self.tax = tax
        self.abbreviation = abbreviation


# NO INCOME TAX
Alaska = StateIncomeTax("Alaska", "AK", 0.00)
Florida = StateIncomeTax("Florida","FL",0.00)
Nevada = StateIncomeTax("Nevada","NV",0.00)
South_Dakota = StateIncomeTax("South Dakota", "SD", 0.00)
Tennessee = StateIncomeTax("Tennessee", "TN", 0.00)
Texas = StateIncomeTax("Texas", "TX", 0.00)
Washington = StateIncomeTax("Washington","WA", 0.00)
Wyoming = StateIncomeTax("Wyoming", "WY", 0.00)
# -------------------------------
# FLAT INCOME TAX
New_Hampshire = StateIncomeTax("New Hampshire", "NH", 0.05)
Colorado = StateIncomeTax("Colorado", "CO", 0.0455)
Illinois = StateIncomeTax("Illinois", "IL", 0.0495)
Indiana = StateIncomeTax("Indiana", "IN", 0.0323)
Kentucky = StateIncomeTax("Kentucky", "KY", 0.05)
Massachusetts = StateIncomeTax("Massachusetts", "MA", 0.05)
Michigan = StateIncomeTax("Michigan", "MI", 0.0425)
North_Carolina = StateIncomeTax("North Carolina", "NC", 0.0525)
Pennsylvania = StateIncomeTax("Pennsylvania", "PA", 0.0307)
Utah = StateIncomeTax("Utah", "UT", 0.0495)
# ------------------------------
# BRACKETED INCOME TAX
Alabama = StateIncomeTax("Alabama", "AL", 0.0367)
Arizona = StateIncomeTax("Arizona", "AZ", 0.0515)
Arkansas = StateIncomeTax("Arkansas", "AR", 0.0397)
California = StateIncomeTax("California", "CA", 0.09)
Connecticut = StateIncomeTax("Connecticut", "CT", 0.0479)
Delaware = StateIncomeTax("Delaware", "DE", 0.0389)
Georgia = StateIncomeTax("Georgia", "GA", 0.287)
Hawaii = StateIncomeTax("Hawaii", "HI", 0.078)
Idaho = StateIncomeTax("Idaho", "ID", 0.314)
Iowa = StateIncomeTax("Iowa", "IA", 0.0578)
Kansas = StateIncomeTax("Kansas", "KS", 0.0451)
Louisiana = StateIncomeTax("Louisiana", "LA", 0.04)
Maine = StateIncomeTax("Maine", "ME", 0.06)
Maryland = StateIncomeTax("Maryland", "MD", 0.0413)
Minnesota = StateIncomeTax("Minnesota", "MN", 0.0763)
Mississippi = StateIncomeTax("Mississippi", "MS", 0.04)
Missouri = StateIncomeTax("Missouri", "MO", 0.0387)
Montana = StateIncomeTax("Montana", "MT", 0.043)
Nebraska = StateIncomeTax("Nebraska", "NE", 0.0531)
New_Jersey = StateIncomeTax("New Jersey", "NJ", 0.0735)
New_Mexico = StateIncomeTax("New Mexico", "NM", 0.0378)
New_York = StateIncomeTax("New York", "NY", 0.0631)
North_Dakota = StateIncomeTax("North Dakota", "ND", 0.0189)
Ohio = StateIncomeTax("Ohio", "OH", 0.0283)
Oklahoma = StateIncomeTax("Oklahoma", "OK", 0.05)
Oregon = StateIncomeTax("Oregon", "OR", 0.079)
Rhode_Island = StateIncomeTax("Rhode Island", "RI", 0.453)
South_Carolina = StateIncomeTax("South Carolina", "SC", 0.07)
Vermont = StateIncomeTax("Vermont", "VT", 0.0532)
Virginia = StateIncomeTax("Virginia", "VA", 0.0575)
West_Virginia = StateIncomeTax("West Virginia", "WV", 0.0585)
Wisconsin = StateIncomeTax("Wisconsin", "WI", 0.0585)
# ---------------------------------------
# LIST OF STATES
list_states = [Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut,
               Delaware, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa,
               Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan,
               Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada,
               New_Hampshire, New_Jersey, New_Mexico, New_York, North_Carolina,
               North_Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode_Island,
               South_Carolina, South_Dakota, Tennessee, Texas, Utah, Vermont,
               Virginia, Washington, West_Virginia, Wisconsin, Wyoming]
# ---------------------------------------
def calculate_state_tax(income, ListState: list, state):
    for item in ListState:
        if state == item.name or state == item.abbreviation:
            total_inc = (1 - item.tax) * income
            return total_inc
    return "Please Enter a Valid State"

def calculate_federal_tax(income):
    if income <= 9875:
        return income * 0.9
    elif income > 9875 and income < 40126:
        return income * 0.88
    elif income > 40125 and income < 85526:
        return income * 0.78
    elif income > 85525 and income < 163301:
        return income * 0.76
    elif income > 163300 and income < 207351:
        return income * 0.68
    elif income > 207350 and income < 518401:
        return income * 0.65
    elif income > 518400:
        return income * 0.63

def calculate_Taxes(income, ListState: list, state):
    After_FED = calculate_federal_tax(income)
    Total_Inc = calculate_state_tax(After_FED, ListState, state)
    return Total_Inc

if __name__ == '__main__':
    inc = int(input())
    state = input()

    print(calculate_Taxes(inc, list_states, state))

