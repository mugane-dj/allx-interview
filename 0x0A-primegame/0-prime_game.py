#!/usr/bin/python3
"""
Prime Game module
"""


def isWinner(x, nums):
    """
    isWinner - determines the winner of the game if both players play
               optimally.
    :param: x - number of rounds to be played.
    :param: nums - an array of n (number picked in each round to form the set)
    """

    def isPrime(n):
        if n < 2:
            return False
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

    for i in range(x):
        n = nums[i]
        set = list(range(1, n + 1))
        primes = list(filter(isPrime, set))
        for prime in primes:
            set = [num for num in set if num % prime != 0]

        if len(set) == 1:
            return None
        elif len(set) % 2 == 0:
            return "Maria"
        else:
            return "Ben"
