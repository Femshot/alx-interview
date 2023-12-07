#!/usr/bin/python3
"""A module containing the function canUnlockAll"""


def canUnlockAll(boxes):
    """A function to check if all locked boxes can be unlocked

    boxes conatain positive integers called keys
    and are numbered sequentially from 0 to n - 1
    boxes should contain key(s) to other box(es)
    A key with the same number as a box opens that box

    Args:
        boxes: List of list

    Return:
        True if all boxes can be opened else false
    """
    haveKey = [0]
    lockedBox = []
    unlockedAll = False
    for index, box in enumerate(boxes):
        if index in haveKey:
            for key in box:
                haveKey.append(key)
            unlockedAll = True
        else:
            lockedBox.append(index)
            unlockedAll = False

    for box in lockedBox:
            unlockedAll = True if box in haveKey else False

    return unlockedAll
