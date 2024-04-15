#!/usr/bin/python3
"""
Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Represents a base geometry class with public instance
    methods 'area' and 'integer_validator'.
    """
    def area(self):
        """Raises an exception when called."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
