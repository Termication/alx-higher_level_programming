#!/usr/bin/python3
"""Contains the function find_peak, which finds a peak in a list of
unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.
    A peak element is an element that is greater than or equal to its
    neighbors.
    """
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = size // 2
    peak = list_of_integers[mid]

    if peak >= list_of_integers[mid - 1] and peak >= list_of_integers[mid + 1]:
        return peak
    elif mid > 0 and list_of_integers[mid - 1] > peak:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
