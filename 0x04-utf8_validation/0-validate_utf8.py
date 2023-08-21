#!/usr/bin/python3
"""
UTF-8 Validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    The function `validUTF8` checks if a given list of integers
    represents a valid UTF-8 encoding.

    :param data: The `data` parameter is a list of integers
    :type data: List[int]
    :return: a boolean value. It returns True if the given data
             is a valid UTF-8 encoding, and False otherwise.
    """
    count = 0
    for i in range(len(data)):
        curr = data[i]

        if count == 0:
            if curr >> 5 == 0b110:
                count = 1
            elif curr >> 4 == 0b1110:
                count = 2
            elif curr >> 3 == 0b11110:
                count = 3
            elif curr >> 7 != 0:
                return False
        else:
            if curr >> 6 != 0b10:
                return False
            count -= 1
    return True
