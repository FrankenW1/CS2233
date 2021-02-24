lst = ['This is the first string in the list', 'This is the last string in the list']
#x = input('enter start, first, or end: ')


def first(my_list, x2):
    x2 = x2.lower()
    if not my_list:
        return None
    if x2 == 'start':
        return my_list[0]

    if x2 == 'first':
        return my_list[0]

    if x2 == 'end':
        return my_list[-1]


# while True:

# if x2 == 'start' or 'first':
#     print(lst[0])
#    break

#  if x2 == 'end':
#    print(lst[-1])
#   break

# else:
#   print("you have made an invalid choice")
#   break
