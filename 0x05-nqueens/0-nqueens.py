#!/usr/bin/python3
""" Algorithm to solve the N queens problem """
import sys


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    value = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if value < 4:
    print('N must be at least 4')
    exit(1)


def solveNQueens(n):
    def could_place(row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if could_place(row, col):
                board[row] = col
                place_queens(n, row + 1)
                board[row] = 0

    result = []
    board = [0] * n
    place_queens(n, 0)
    new_row = []
    for sol in result:
        i = 0
        new_col = []
        for val in sol:
            new_col.append([i, val])
            i += 1
        new_row.append(new_col)
    return new_row


outcomes = solveNQueens(value)
for i in outcomes:
    print(i)
