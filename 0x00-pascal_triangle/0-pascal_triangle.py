#!/usr/bin/python3
"""A module containing Pascal triangle function"""


def factorial(a):
    """Returns factorial of a number"""
    res = 1
    while a > 0:
        res = res * a
        a -= 1

    return res


def pascal_triangle(n):
    """Function Implementing Pascal traingle formula

    Args:
        n(int): Number to calculate pascal triangle up to

    Return: List of list of triangle
    """
    if n <= 0:
        return []

    triangle = [(factorial(x)//(factorial(y)*factorial(x-y))
                for y in range(x+1)) for x in range(1, n)]

    triangle[0:0] = [[1]]
    return triangle
