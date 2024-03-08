"""
linear_search.py - Implementation of the linear search algorithm

This module contains the implementation of the linear search algorithm,
ehich searches for a target value in a list by sequentially checking each
element until a match is found or the end of the list is reached.

Author: Kinyarasam
"""
from typing import List, Any


def linear_search(arr: List, target: Any) -> int:
    """
    Perform linear search to find the target element in the given list.

    Args:
        arr (list): The list to be searched,
        target: The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example Usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    target = 3

    index = linear_search(my_list, target)
    if index != -1:
        print("Element {t} found at index {i}".format(t=target, i=index))
    else:
        print("Element {t} not found".format(target))
