#!/usr/bin/python3
"""
Square Module

This module contains a Square class that defines a geometric square shape.
The Square class includes functionality to set and get the size and position
of the square, compute its area, and print it on the screen.
"""


class Square():
    """
    Represents a square.

    Attributes:
        size (int): The length of one side of the square.
        position (tuple): The coordinates of the
        top-left corner of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the given size and position.

        Args:
            size (int): The size of one edge of the square.
            position (tuple): The coordinates of the
            top-left corner of the square.
        """
        self.size = size
        self.position = position

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        square_str = ""

        if self.__size > 0:
            for y in range(self.__position[1]):
                square_str += '\n'
            for x in range(self.__size):
                square_str += ' ' * self.__position[0]
                square_str += '#' * self.__size + '\n'

        return square_str[:-1]

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
        if isinstance(value, int):
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
            value (tuple): The coordinates of the
            top-left corner of the square.

        Raises:
            TypeError: If position is not a tuple of 2 integers.
        """
        if isinstance(value, tuple) and len(value) == 2 and \
                isinstance(value[0], int) and isinstance(value[1], int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 integers")

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
