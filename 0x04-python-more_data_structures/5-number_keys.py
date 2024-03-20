#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    num_keys = list(a_dictionary.keys())

    for i in num_keys:
        number += 1

    return (number)
