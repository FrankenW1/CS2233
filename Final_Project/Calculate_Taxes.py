class StateIncomeTax:
    def __init__(self,name: str, abbreviation: str, tax: float):
        self.name = name
        self.tax = tax
        self.abbreviation = abbreviation


# NO INCOME TAX
Alaska = StateIncomeTax("ALASKA", "AK", 0.00)
Florida = StateIncomeTax("FLORIDA","FL",0.00)
Nevada = StateIncomeTax("NEVADA","NV",0.00)
South_Dakota = StateIncomeTax("SOUTH DAKOTA", "SD", 0.00)
Tennessee = StateIncomeTax("TENNESSEE", "TN", 0.00)
Texas = StateIncomeTax("TEXAS", "TX", 0.00)
Washington = StateIncomeTax("WASHINGTON","WA", 0.00)
Wyoming = StateIncomeTax("WYOMING", "WY", 0.00)
# -------------------------------
# FLAT INCOME TAX
New_Hampshire = StateIncomeTax("NEW HAMPSHIRE", "NH", 0.05)
Colorado = StateIncomeTax("COLORADO", "CO", 0.0455)
Illinois = StateIncomeTax("ILLINOIS", "IL", 0.0495)
Indiana = StateIncomeTax("INDIANA", "IN", 0.0323)
Kentucky = StateIncomeTax("KENTUCKY", "KY", 0.05)
Massachusetts = StateIncomeTax("MASSACHUSETTS", "MA", 0.05)
Michigan = StateIncomeTax("MICHIGAN", "MI", 0.0425)
North_Carolina = StateIncomeTax("NORTH CAROLINA", "NC", 0.0525)
Pennsylvania = StateIncomeTax("PENNSYLVANIA", "PA", 0.0307)
Utah = StateIncomeTax("UTAH", "UT", 0.0495)
# ------------------------------
# BRACKETED INCOME TAX
Alabama = StateIncomeTax("ALABAMA", "AL", 0.0367)
Arizona = StateIncomeTax("ARIZONA", "AZ", 0.0515)
Arkansas = StateIncomeTax("ARKANSAS", "AR", 0.0397)
California = StateIncomeTax("CALIFORNIA", "CA", 0.09)
Connecticut = StateIncomeTax("CONNECTICUT", "CT", 0.0479)
Delaware = StateIncomeTax("DELAWARE", "DE", 0.0389)
Georgia = StateIncomeTax("GEORGIA", "GA", 0.287)
Hawaii = StateIncomeTax("HAWAII", "HI", 0.078)
Idaho = StateIncomeTax("IDAHO", "ID", 0.314)
Iowa = StateIncomeTax("IOWA", "IA", 0.0578)
Kansas = StateIncomeTax("KANSAS", "KS", 0.0451)
Louisiana = StateIncomeTax("LOUISIANA", "LA", 0.04)
Maine = StateIncomeTax("MAINE", "ME", 0.06)
Maryland = StateIncomeTax("MARYLAND", "MD", 0.0413)
Minnesota = StateIncomeTax("MINNESOTA", "MN", 0.0763)
Mississippi = StateIncomeTax("MISSISSIPPI", "MS", 0.04)
Missouri = StateIncomeTax("MISSOURI", "MO", 0.0387)
Montana = StateIncomeTax("MONTANA", "MT", 0.043)
Nebraska = StateIncomeTax("NEBRASKA", "NE", 0.0531)
New_Jersey = StateIncomeTax("NEW JERSEY", "NJ", 0.0735)
New_Mexico = StateIncomeTax("NEW MEXICO", "NM", 0.0378)
New_York = StateIncomeTax("NEW YORK", "NY", 0.0631)
North_Dakota = StateIncomeTax("NORTH DAKOTA", "ND", 0.0189)
Ohio = StateIncomeTax("OHIO", "OH", 0.0283)
Oklahoma = StateIncomeTax("OKLAHOMA", "OK", 0.05)
Oregon = StateIncomeTax("OREGON", "OR", 0.079)
Rhode_Island = StateIncomeTax("RHODE ISLAND", "RI", 0.453)
South_Carolina = StateIncomeTax("SOUTH CAROLINA", "SC", 0.07)
Vermont = StateIncomeTax("VERMONT", "VT", 0.0532)
Virginia = StateIncomeTax("VIRGINIA", "VA", 0.0575)
West_Virginia = StateIncomeTax("WEST VIRGINIA", "WV", 0.0585)
Wisconsin = StateIncomeTax("WISCONSIN", "WI", 0.0585)
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

