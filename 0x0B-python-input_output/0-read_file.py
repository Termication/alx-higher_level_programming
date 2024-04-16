#!/usr/bin/python3

"""Defines a function for reading text files."""


def read_file(filename=""):
    """
    Print the contents of a UTF-8 encoded text file to stdout.

    Args:
        filename (str): The name of the file to be read.
        Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
