#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    In a text file, there is a single character H.
    Your text editor can execute only two operations in this file:
    Copy All and Paste.
    Given a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    """
    if m <= 1:
        return 0

    for i in range(2, m + 1):
        if m % x == 0:
            return minOperations(int(m / x)) + x
    return m