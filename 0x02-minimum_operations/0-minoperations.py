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
    if n <= 1:
        return 0

    for x in range(2, n + 1):
        if n % x == 0:
            return minOperations(int(n / x)) + x
    return n
