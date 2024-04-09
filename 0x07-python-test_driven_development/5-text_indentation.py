#!/usr/bin/python3
"""
This module provides functionality for formatting text by splitting it into lines.
"""

def text_indentation(text):
    """
    Splits a text into lines based on '?', ':', and '.', followed by two new lines.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("The 'text' argument must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1

        if flag == 1:
            if char in ['?', '.', ':']:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
