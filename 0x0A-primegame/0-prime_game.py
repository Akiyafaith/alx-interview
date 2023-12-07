#!/usr/bin/python3
""" Prime Game """


def is_prime(num, primes):
    """Check if a given number is prime."""
    for prime in primes:
        if prime * prime > num:
            return True
        if num % prime == 0:
            return False
    return True


def isWinner(x, nums):
    most_wins = 0
    winner = None

    for n in nums:
        primes = [2]  # Initialize with the first prime number

        # Find all primes up to n using the Sieve of Eratosthenes
        for num in range(3, n + 1, 2):
            if is_prime(num, primes):
                primes.append(num)

        # Determine the winner based on remaining primes
        maria_wins = sum(not is_prime(i, primes) for i in range(1, n + 1))
        ben_wins = n - maria_wins

        if maria_wins > ben_wins:
            current_winner = "Maria"
        elif ben_wins > maria_wins:
            current_winner = "Ben"
        else:
            current_winner = None

        # Update overall winner
        if current_winner:
            most_wins += 1
            winner = current_winner

    return winner
