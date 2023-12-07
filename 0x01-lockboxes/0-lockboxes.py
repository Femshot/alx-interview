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
    for index, box in enumerate(boxes):
        if index in haveKey:
            haveKey.extend(box)
        else:
            lockedBox.append(index)

    for box in lockedBox.copy():
        if box in haveKey:
            haveKey.extend(boxes[box])
            lockedBox.remove(box)

    if lockedBox:
        return False
    else:
        return True
