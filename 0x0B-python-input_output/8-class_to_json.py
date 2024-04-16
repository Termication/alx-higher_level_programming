#!/usr/bin/python3

"""
Defines a function for converting Python classes
to JSON-compatible dictionaries.
"""


def class_to_json(obj):
    """
    Convert a Python class instance to a JSON-compatible dictionary.

    Args:
        obj: The Python class instance to convert.

    Returns:
        dict: The dictionary representation of the class instance.
    """
    return obj.__dict__
