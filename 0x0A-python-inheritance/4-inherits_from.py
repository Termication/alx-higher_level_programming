#!/usr/bin/python3
"""
Defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is a subclass of
    a_class, otherwise returns False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
