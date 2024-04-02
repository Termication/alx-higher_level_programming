#!/usr/bin/python3
"""
List Division Module

This module defines a function list_division that divides two lists
element-wise and returns a new list containing the results.
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element-wise.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list containing the results of the divisions.
    """
    result_list = []

    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("TypeError: Cannot divide elements of different types.")
            division = 0
        except ZeroDivisionError:
            print("ZeroDivisionError: Cannot divide by zero.")
            division = 0
        except IndexError:
            print("IndexError: Lists are of different lengths.")
            division = 0
        finally:
            result_list.append(division)

    return result_list
