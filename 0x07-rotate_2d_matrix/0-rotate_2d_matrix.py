#!/usr/bin/python3
'''Module containing rotate_2d_matrix function '''


def rotate_2d_matrix(matrix):
    '''Given an n x n 2D matrix, rotate it 90 degrees clockwise'''
    n = len(matrix)
    i, j, x = 0, 0, 0
    copy_matrix = [[x for x in y] for y in matrix]

    while i <= n:
        if x == n:
            break
        matrix[x].pop(i)
        matrix[x].insert(0, copy_matrix[i][j])
        i += 1
        if i == n and x < n:
            i = 0
            x += 1
            j += 1
