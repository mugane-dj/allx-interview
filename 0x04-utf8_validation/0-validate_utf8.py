#!/usr/bin/python3
"""
UTF-8 Validation
"""
from typing import List


def check_type(num: int) -> int:
    """
    The function `check_type` checks the type of a number by
    comparing it with a list of valid types and returns the
    index of the first valid type found, or -1 if no valid
    type is found.

    :param num: The parameter `num` is an integer
    :type num: int
    :return: The function `check_type` returns an integer value.
    """
    valid_types = [128, 64, 32, 16, 8]
    for i in range(5):
        if (valid_types[i] & num) == 0:
            return i
    return -1


def validUTF8(data: List[int]) -> bool:
    """
    The function `validUTF8` checks if a given list of integers
    represents a valid UTF-8 encoding.

    :param data: The `data` parameter is a list of integers
    :type data: List[int]
    :return: a boolean value. It returns True if the given data
             is a valid UTF-8 encoding, and False otherwise.
    """
    data_len = len(data)
    for i in range(data_len):
        curr = data[i]
        type = check_type(curr)

        if type == 0:
            continue
        elif type > 1 & i + type <= data_len:
            while type > 1:
                if check_type(data[i + type - 1]) != 1:
                    return False
                type -= 1
        else:
            return False
    return True
