#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    The function `canUnlockAll` checks if all the boxes in a given list can
    be unlocked by using the keys inside the boxes.

    :param boxes: The parameter "boxes" is a list of lists. Each inner
                  list represents a box, and the indices of the inner
                  list represent the keys that can open that box.
                  For example, if boxes[0] = [1,2], it means that the
                  first box can be opened with keys 1 and 2.
    :return: a boolean value. It returns True if all the boxes
             can be unlocked, and False otherwise.
    """

    n = len(boxes)

    keys = [0]  # Keys correspond to the indexes of all boxes

    for i in keys:
        for key in boxes[i]:  # Check all keys in all boxes
            if key not in keys and i <= n - 1:
                keys.append(key)

    if len(keys) == n:
        return True
    return False
