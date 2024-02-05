#!/usr/bin/python3
""" Module containing a function island_perimeter """


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid """
    y = 0
    found_sq = []

    while y < len(grid):
        x = 0
        while x < len(grid[0]):
            if grid[y][x]:
                break
            x += 1
        if x < len(grid[0]) and grid[y][x]:
            break
        y += 1

    return find_next_sq(y, x, found_sq, grid)


def find_next_sq(y, x, found, grid):
    """ Finds all connected island and returns the perimeter """
    other_sq = []
    perimeter = 0

    found.append((y, x))
    other_sq = check_neigh(y, x, grid, found)
    for points in other_sq:
        perimeter += find_next_sq(*points, found, grid)
    perimeter += add_perimeter(len(other_sq))
    return perimeter


def check_neigh(a, b, grid, found_sq):
    """ Checks the surrounding points of a cell to find land cells

    Args:
        a: Column of the current cell
        b: Row of the current cell
        grid: matrix grid of water and island
        found_sq: list of found island cells

    Return:
        list of all neigbouring land cells not found yet
    """
    next_sqs = []
    if grid[a][b-1] and (a, b-1) not in found_sq:
        next_sqs.append((a, b-1))
    if grid[a][b+1] and (a, b+1) not in found_sq:
        next_sqs.append((a, b+1))
    if grid[a-1][b] and (a-1, b) not in found_sq:
        next_sqs.append((a-1, b))
    if grid[a+1][b] and (a+1, b) not in found_sq:
        next_sqs.append((a+1, b))

    return next_sqs


def add_perimeter(n):
    """ Adds available perimeter calculated from a cell

        Calculation is done based on presence of surrounding land cells
        where 3 lands are connected only 1 side of the cell counts as perimeter
    """
    if n == 4 or n == 0:
        return 0
    elif n == 3:
        return 1
    elif n == 2:
        return 2
    elif n == 1:
        return 3
