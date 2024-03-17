#!/usr/bin/python3
def element_at(my_list, index):
    if index < 0 or index > len(my_list) - 1:
        return 'None'
    else:
        return my_list[index]
