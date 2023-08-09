#!/usr/bin/python3
"""
minOperations - calculates the minimum number of operations required to obtain
                a string of length n consisting of the character "H" using the
                operations of copying all and pasting.
"""


def minOperations(n: int) -> int:
    """
    The function `minOperations` calculates the minimum number of
    operations required to obtain a string of length `n` consisting
    of the character "H" using the operations of copying all and pasting.

    :param n: The parameter `n` represents the number of characters
              you want to obtain in the string
    :type n: int
    :return: the minimum number of operations required to obtain a
             string of length n, where the operations allowed are
             copying all the characters and pasting them.
    """
    copy_all = 0
    paste = 0
    char_string = "H"

    while (n > 1):
        if (len(char_string) % 2):
            char_string *= 2
            n //= 2
        else:
            char_string += "H"
            n -= 1

        copy_all += 1
        paste += 1
    return copy_all + paste
