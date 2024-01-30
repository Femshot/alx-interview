#!/usr/bin/python3
"""Module containing makeChange function"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet total

    Args
    coins(list): A list of coins
    total(int): An integer value

    Return: Number of coins needed if total met,
            Else 0 if total less than or equal to 0
            -1 if total can't be met with given coins
    """
    if total <= 0:
        return 0

    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        while (coin <= total):
            total -= coin
            count += 1
        if total == 0:
            return count

    return -1
