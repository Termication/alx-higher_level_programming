#!/usr/bin/python3
def new_in_list(my_list, index, element):
    copy = my_list.copy()
    if index < 0 or index > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[index] = element
        return copy
