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


# PROBLEM 1 - 10 pts
# Complete the function below to filter the list_of_names defined on line 1.
# This function will filter the list based on the input_str. If the name starts with
# the input string the result will be included return statement of the function.
def filter_list_of_names(input_str: str) -> List[str]:
    tl = []
    i = 0
    for i in range(len(list_of_names)):
        if list_of_names[i].startswith(input_str):
            tl.append(list_of_names[i])
    return tl


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


def first(items: Iterable, default=None, condition=None):
    if default is None and callable(condition) is False:
        return items[0]
    elif default != None and items == []:
        print('default =', default)
        return default


def default_filter(x):
    return True


def first(items: Iterable,*, default=..., condition: callable = None):
    condition = condition or default_filter
    try:
        return next(i for i in items if condition(i))
    except StopIteration:
        if default == ...:
            raise
        return default



def test_first():
    x = ['a', 'b']
    print(first(x) == 'a')


def first_is_empty():
    x = []
    print(type(first(x)))
    # print(first(x, default=None) is None)
    print(first(x) is None)


# BONUS PROBLEM - 100% on the exam
# Write a function named "first" that takes an iterable called items and optional key
# word arguments "default" and "condition" If default and condition are not defined, the function will
# return the first item in the list. If default is defined and a empty list is passed into the function,
# the default value will be returned. This function will return type Any or raise a StopIteration exception.
#
# default will have a annotation of Any
# condition will be of type callable
#
# Everything must be correctly defined on function along with passing many different cases. The best attempt
# of the class will also receive and additional 5 pts on the exam.

if __name__ == "__main__":
    a = 0
    # write any tests here
    # print(remove_vision(list_of_names))
    # print(filter_list_of_names('a'))
