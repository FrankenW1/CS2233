from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Final_Project.Calculate_Taxes import list_states


tax_router = APIRouter(prefix="/tax")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
states = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNECTICUT", "DELAWARE", "FLORIDA",
          "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", "MAINE",
          "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA",
          "NEVADA", "NEW HAMPSHIRE", "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", "OHIO",
          "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS",
          "UTAH", "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]
state_abb = ["AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
              "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
              "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX",
              "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
@tax_router.get("/calculate")
def calc_tax(state: str, income: int or float):
    # if (state.upper() in states) or (state.upper() in state_abb):
    #     tax = income * .15
    #     r_income = income - tax
    #     return {"remaining": float("{:.2f}".format(r_income)),
    #             "tax": float("{:.2f}".format(tax)),
    #             "state": f"{state}"}
    for item in list_states:
        if state == item.name.upper() or state == item.abbreviation.upper():
            total_inc = (1 - item.tax) * income
            return list_states[item]
app.include_router(tax_router)
if __name__ == "__main__":
    uvicorn.run("serv:app", host="0.0.0.0", reload="true")
