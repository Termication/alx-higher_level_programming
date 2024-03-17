#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_iknow = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_iknow.append(True)
        else:
            list_iknow.append(False)
    return list_iknow
