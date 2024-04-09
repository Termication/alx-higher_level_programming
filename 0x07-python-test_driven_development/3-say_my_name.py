#!/usr/bin/python3
"""
This module defines a function for printing a name.
"""


def say_my_name(first_name, last_name=""):
    '''
    Print a person's name in the format "<first name> <last name>".

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.
    '''

    if not isinstance(first_name, str):
        raise TypeError("The first_name argument must be a string")

    if not isinstance(last_name, str):
        raise TypeError("The last_name argument must be a string")

    print(f"My name is {first_name} {last_name}")
