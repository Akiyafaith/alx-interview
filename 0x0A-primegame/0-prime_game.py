#!/usr/bin/python3
"""Prime Game"""


def is_prime(num):
    """check if a given number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(is_prime(i) for i in range(1, n + 1))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
