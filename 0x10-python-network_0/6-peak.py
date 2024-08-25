#!/usr/bin/python3
"""Contains the function find_peak, which finds a peak in a list of
unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers
    A peak element is an element that is greater than or equal to its
    neighbors.
    """
    li = list_of_integers
    n = len(li)

    if n == 0:
        return None

    mid = n // 2

    if (mid == n - 1 or li[mid] >= li[mid + 1]) and \
       (mid == 0 or li[mid] >= li[mid - 1]):
        return li[mid]

    if mid != n - 1 and li[mid + 1] > li[mid]:
        return find_peak(li[mid + 1:])

    return find_peak(li[:mid])
