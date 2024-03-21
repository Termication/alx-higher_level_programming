#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numOne = 0
    numTwo = 0

    for tup in my_list:
        numOne += tup[0] * tup[1]
        numTwo += tup[1]

    return (numOne / numTwo)
