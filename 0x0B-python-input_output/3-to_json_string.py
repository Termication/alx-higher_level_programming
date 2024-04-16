#!/usr/bin/python3

"""Defines a function for converting objects to JSON strings."""
import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON string representation.

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
