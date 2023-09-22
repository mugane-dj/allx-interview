#!/usr/bin/python3
"""
Least coins module
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determines the fewest number of coins needed
    to meet the given amount `total` using dynamic programming approach
    """
    m = len(coins)

    # create solution matrix
    a = [[0 for _ in range(total + 1)] for _ in range(m)]

    for i in range(m):
        for j in range(total + 1):
            if i == 0 and j == 0:
                a[i][j] = 0
            elif i == 0:
                if coins[i] > j:
                    a[i][j] = -1
                else:
                    a[i][j] = a[i][j - coins[i]] + 1
            else:
                if coins[i] > j:
                    a[i][j] = a[i - 1][j]
                else:
                    a[i][j] = min(a[i - 1][j], 1 + a[i][j - coins[i]])
    return a[m - 1][total]
