from typing import List, Callable, Any, Iterable

# BE CAREFUL OF SCOPE WHEN WORKING ON THESE PROBLEMS
list_of_names: List[str] = [
    "alex",
    "amanda",
    "aaron",
    "charlie",
    "vision",
    "wanda",
    "tommy",
    "sophie",
]



# PROBLEM 2 - 5 pts
# Complete a function below.
# Remove the name "vision" from the list on line 1. Return the remaining items of the list
def remove_vision(my_list) -> List[str]:
    ret = []
    for items in my_list:
        ret.append(items)
    ret.remove('vision')
    return ret     # This didn't work because I was removing vision from the global list
                   # Changing it to a local list fixes this issue


# PROBLEM 3 - 10 pts
# Complete a function below.
# Return the last matching element of list_of_names that ends with the input_str.
# example if the input_str = 'x' the output would be 'alex'
# example if the input_str = 'a' the output would be 'wanda'
def return_last_match(input_str: str) -> str:
    tl = []
    for i in range(len(list_of_names)):
        t = list_of_names[i]
        if input_str == t[-1]:
            tl.append(t)
        for i in range(len(tl)):
            return tl[i]
    # forgot to return values as string and not list

