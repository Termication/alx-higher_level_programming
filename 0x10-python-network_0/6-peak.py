#!/usr/bin/python3
"""Contains the function find_peak, which finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.
    
    A peak element is an element that is greater than or equal to its neighbors.
    """
    li = list_of_integers
    l = len(li)
    
    # If the list is empty, return None
    if l == 0:
        return None

    # Find the middle index
    m = l // 2

    # Check if the middle element is a peak
    # A peak element is greater than or equal to its neighbors or if it is at the edges of the list
    if (m == l - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]

    # If the right neighbor is greater, recursively search in the right half
    if m != l - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    
    # Otherwise, recursively search in the left half
    return find_peak(li[:m])
