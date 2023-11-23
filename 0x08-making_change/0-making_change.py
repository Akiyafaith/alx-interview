#!/usr/bin/python3
"""change comes from within"""
def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total."""
    if total <= 0:
        return 0

    # Create a table, store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the table using dynamic programming
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinite, it means the total cannot be achieved
    return dp[total] if dp[total] != float('inf') else -1
