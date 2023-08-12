#!/usr/bin/python3
"""
minOperations - calculates the minimum number of operations required to obtain
                a string of length n consisting of the character "H" using the
                operations of copying all and pasting.
"""


def minOperations(n: int) -> int:
    """
    The function `minOperations` calculates the minimum number of operations
    required to reach a given number `n` using only three operations: adding 1,
    multiplying by 2, and multiplying by 3.

    :param n: The parameter `n` represents the target number for which we want
              to find the minimum number of operations
    :type n: int
    :return: the minimum number of operations required to reach the number `n`.
    """
    table = [n] * (n + 1)
    table[1] = 0

    for i in range(1, n):
        table[i + 1] = min(table[i + 1], table[i] + 1)
        if i * 2 <= n:
            table[i * 2] = min(table[i] + 1, table[i * 2])
        if i * 3 <= n:
            table[i * 3] = min(table[i] + 1, table[i * 3])

    return table[n]
