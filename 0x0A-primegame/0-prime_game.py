#!/usr/bin/python3
"""Prime Game"""


def is_prime(num, primes):
    """Check if a given number is prime."""
    if num < 2:
        return False
    for i in primes:
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)
    primes = [2]  # Initialize with the first prime number

    for num in range(3, max_num + 1, 2):
        if is_prime(num, primes):
            primes.append(num)

    for n in nums:
        prime_count = sum(is_prime(i, primes) for i in range(1, n + 1))
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
