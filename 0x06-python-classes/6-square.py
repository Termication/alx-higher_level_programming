#!/usr/bin/python3
"""
Square Module

This module contains the definition of the Square class
"""


class Square():
    """
    A class to represent a square.

    Attributes:
        size (int): The length of one side of the square.
        position (tuple): The coordinates of the top-left corner of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the given size and position.

        Args:
            size (int): The size of one edge of the square.
            position (tuple): The coordinates of the top-left corner of squ
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get or set the size of the square.

        Returns:
            int: The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of one edge of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        Get or set the position of the square.

        Returns:
            tuple: The coordinates of the top-left corner of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The coordinates of top-left corner of square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if type(value) is tuple and len(value) == 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with '#' characters.

        Prints the square with its top-left corner at the specified position
        and each side of length equal to the size of the square.
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
