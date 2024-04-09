#!/usr/bin/python3
"""
This module defines a function for printing a square.
"""


def print_square(size):
    """
    Print a square using the '#' character.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer or if it's a float and less than zero.
        ValueError: If size is less than zero.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
