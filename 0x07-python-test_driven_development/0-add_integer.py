#!/usr/bin/python3
'''

This module provides a function to compute the sum of two numbers.

'''


def add_integer(a, b=98):
    '''Calculate the sum of two numbers and return an integer result

    Args:
        a: The first number
        b: The second number (default is 98)

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If either a or b is not an integer or float
    '''
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
