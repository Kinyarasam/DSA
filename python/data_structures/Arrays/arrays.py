#!/usr/bin/env python3
"""
arrays.py - Illustration of Python lists

This script demonstrates the usage of python lists, which are dynamic
arrays that can hold elements of different data types. Lists are commonly
used in Python for storing and manipulating collections of items

Author: Kinyarasam
Data: 04/03/2024
"""


def main():
    """
    Main function to demonstrate Python lists

    This function creates a list, performs basic operations such as
    appending, accessing and traversing elements and demonstrates
    list comprehension.
    """

    # Create a list of integers
    my_list = [1, 2, 3, 4, 5]

    # Append and element to the list
    my_list.append(6)

    # Accessing elements of the list
    first_element = my_list[0]
    last_element = my_list[-1]

    # Traversing the list using a for loop
    for element in my_list:
        print(element)

    # List comprehension to create a new list
    squared_list = [x*2 for x in my_list]
    print(squared_list)


if __name__ == "__main__":
    main()
