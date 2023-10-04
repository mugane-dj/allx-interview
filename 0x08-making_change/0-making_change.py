#!/usr/bin/python3
"""
Least coins module
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determines the fewest number of coins needed
    to meet the given amount `total` using dynamic programming approach
    :param coins: list of the denominations of coins available
    :param total: the amount to be made
    :return: fewest number of coins needed to meet `total`
             -1 if `total` cannot be met by any number of coins
    """
    if total <= 0:
        return 0
    result = []
    coins.sort(reverse=True)
    for coin in coins:
        while total // coin > 0:
            result.append(coin)
            total -= coin

    return len(result) if total == 0 else -1
