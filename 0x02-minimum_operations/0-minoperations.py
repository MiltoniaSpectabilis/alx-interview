#!/usr/bin/python3
"""
Minimum Operations: Calculates the fewest
number of operations to reach n 'H' characters.
"""


def minOperations(n):
    """
    Returns the minimum number of operations (Copy All and Paste)
    to reach n 'H' characters.
    """
    if n < 1:
        return 0
    operations = 0
    current_h = 1
    while current_h < n:
        if n % current_h == 0:
            operations += 1 + (n // current_h - 1)
            break
        else:
            operations += 1
            current_h += 1
    return operations
