#!/usr/bin/python3
"""
Definition of the MyList class.
"""


class MyList(list):
    """Inherits from the list class."""
    def __init__(self):
        """Constructor method for MyList."""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list."""
        print(sorted(self))
