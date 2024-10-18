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

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
