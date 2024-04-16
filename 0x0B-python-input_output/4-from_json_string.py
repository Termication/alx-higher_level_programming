#!/usr/bin/python3

"""Defines a function for converting JSON strings to objects."""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
