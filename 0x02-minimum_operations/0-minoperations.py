#!/usr/bin/python3
"""Defines a function minOperations"""


def minOperations(n):
    """Calculates the min operations required to get n number of 'H'

    Return: Minimum number
    """
    curr = 1     # current number of 'H's on the screen
    clipboard = 0     # number of 'H's in the clipboard
    steps = 0     # number of steps taken to reach n 'H's
    # loop until curr equals n
    while curr < n:
        # if n is divisible by curr, perform copy and paste operations
        if n % curr == 0:
            clipboard = curr
            steps += 1
        # if n is not divisible by curr, perform only paste operation
        curr += clipboard
        steps += 1

    return steps
