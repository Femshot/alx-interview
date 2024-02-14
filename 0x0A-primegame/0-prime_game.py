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
    if not nums or x <= 0:
        return None

    maria = ben = 0
    rounds = x

    for n in nums:
        prime_nums = []

        if rounds == 0:
            break

        for digit in range(2, n+1):
            if isprime(digit):
                prime_nums.append(digit)

        if (len(prime_nums) % 2) == 0:
            ben += 1
        else:
            maria += 1

        rounds -= 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None


def isprime(number):
    """ Determines if a number if a prime number or not """
    for x in range(2, (number // 2) + 1):
        if number % x == 0:
            return False
    return True
