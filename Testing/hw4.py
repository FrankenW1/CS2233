list_of_names = ["koda", "sophie", "annika", "aaron", "savannah"]
list_of_names2 = ["koda", "sophie", "annika", "aaron", "savannah"]


def filter_list_of_names1():
    list_of_names.remove("koda")
    return list_of_names


def filter_list_of_names2():
    return [x for x in list_of_names if x != "koda"]


def filter_list_of_names3():
    return list(filter(lambda x: x != "koda", list_of_names))


if __name__ == "__main__":
    print("running Main")
    r11 = filter_list_of_names1()
    r12 = filter_list_of_names2()
    r13 = filter_list_of_names3()
    print(r11 == r12, r11, r12, "QUESTION 1: Do arrays that have the same values equal?")
    print(list_of_names == list_of_names2, list_of_names, list_of_names2, "QUESTION 2: Why are these different arrays?")
    print(id(r11) == id(list_of_names), "QUESTION 3: Why are these the same arrays?")
    print(id(r11) == id(r13), id(r11), id(r13), "QUESTION 4: Why are these different arrays?")
    try:
        filter_list_of_names1()  # QUESTION 5: Why is this an exception?
    except ValueError:
        a = 0
