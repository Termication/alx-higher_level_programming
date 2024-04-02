#!/usr/bin/python3
"""This script defines a Square class."""


class Square:
    """A class to represent squares.

    Attributes:
        __size (int): The length of each side of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int): The length of each side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be non-negative")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
