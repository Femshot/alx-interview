#!/usr/bin/python3
""" A module to compute the winner between two people in a game of prime
numbers and their common factors elimination """


def isWinner(x, nums):
    """ Determines winner between Ben & maria in a prime numbers game

    Args:
        x(int): Number of rounds of game
        nums(list): List of numbers that are the upper limit for each round
                    in arange of 1 - upper limit

    Return: Maria or Ben depending on who won most rounds, None if no winner
    """
    if not nums or (len(nums) != x):
        return None

    winner = {'Maria': 0, 'Ben': 0}

    for n in nums:
        prime_nums = []

        for digit in range(1, n+1):
            if isprime(digit):
                prime_nums.append(digit)

        if (len(prime_nums) % 2) == 0:
            winner['Ben'] += 1
        else:
            winner['Maria'] += 1

    if winner['Maria'] > winner["Ben"]:
        return 'Maria'
    elif winner['Ben'] > winner["Maria"]:
        return 'Ben'
    else:
        return None


def isprime(number):
    """ Determines if a number if a prime number or not """
    if number == 1:
        return False
    for x in range(2, (number // 2) + 1):
        if number % x == 0:
            return False
    return True
