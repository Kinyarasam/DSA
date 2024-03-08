"""
binary_search.py - Implemenetation of the binary search algorithm

This module contains the implementation of the binary search algorithm,
which searches for a target value in a sorted list by repeatedly dividing
the search interval in half until the target is found or the interval is empty.

Author: Kinyarasam
"""
from typing import List, Any


def binary_search(arr: List, target: Any):
    """
    Perform binary search to find the target element in the given sorted list.

    Args:
        arr (list): The sorted list to be searched.
        target (Any): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    target = 3

    index = binary_search(my_list, target)
    if index != -1:
        print("Element {t} found at index {i}".format(t=target, i=index))
    else:
        print("Element {t} not found".format(target))