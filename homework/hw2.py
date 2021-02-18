from typing import Optional, List, Any


def number_length(num: int) -> int:
    num = str(num)
    q = len(num)
    q = int(q)

    return q

    """
    Create a function that takes a number and returns its length.
    :param num:
    :return:

    examples:
    number_length(10) -> 2
    number_length(5000) -> 4
    number_length(0) -> 1
    """
    pass


def list_of_multiples(num: int, length: Optional[int]) -> List[int]:
    x = 0
    z = []
    while x < length:
        z.append(num * (x + 1))
        x = x + 1

    return z
    

    """
    Create a function that takes two numbers as arguments (num, length)
    and returns a list of multiples of num until the list length reaches length.
    :param num:
    :param length:
    :return:

    list_of_multiples(7, 5) -> [7, 14, 21, 28, 35]
    list_of_multiples(12, 10) -> [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    ist_of_multiples(4, None) -> []
    """
    pass


def normalize(input_str) -> str:

    if input_str.upper() == input_str:
        input_str = input_str.lower() + '!'
        input_str = input_str.capitalize()
        return input_str
    else:
        return input_str


    """
    Create a function that takes a string. If the string is all uppercase characters,
     convert it to lowercase and add an exclamation mark at the end.

    :param foo:
    :return:
    normalize("CAPS LOCK DAY IS OVER") -> "Caps lock day is over!"
    normalize("Today is not caps lock day.") -> "Today is not caps lock day."

    """
    pass


def cat_dog(num: int) -> str:
    if (num % 3 == 0) and (num % 5 == 0):
        z = 'CatDog'
        return z
    elif num % 3 == 0:
        z = 'Cat'
        return z
    elif num % 5 == 0:
        z = 'Dog'
        return z
    else:
        return num

    """
    Create a function that takes a number as an argument and returns "Cat", "Dog" or "CatDog".

    If the number is a multiple of 3 the output should be "Cat".
    If the number given is a multiple of 5, the output should be "Dog".
    If the number given is a multiple of both 3 and 5, the output should be "CatDog".
    If the number is not a multiple of either 3 or 5, the number should be output
    on its own as shown in the examples below.
    The output should always be a string even if it is not a multiple of 3 or 5.

    :param num:
    :return:
    cat_dog(4) -> "4"
    cat_dog(3) -> "Cat"
    cat_dog(5) -> "Dog"
    cat_dog(15) -> "CatDog"
    """
    pass

