#!/usr/bin/python3
""" Module containing a function island_perimeter """


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid """
    y = 0
    found_sq = []

    if (not grid) or (not grid[0]):
        return 0

    len_grid, len_row = len(grid), len(grid[0])
    while y < len(grid):        # Checks for first island block then exits
        x = 0
        while x < len_grid:
            if grid[y][x]:
                break
            x += 1
        if x < len_row and grid[y][x]:
            break
        y += 1

    if y >= len_grid or x >= len_row:
        return 0

    return find_next_sq(y, x, found_sq, grid)


def find_next_sq(y, x, found, grid):
    """ Finds all connected island and returns the perimeter """
    other_sq = []
    perimeter = 0

    if (y, x) in found:
        return 0
    found.append((y, x))
    other_sq = check_neigh(y, x, grid, found)
    perimeter += 4 - len(other_sq)          # 4 is for single isolated island
    for a, b in set(other_sq) - set(found):
        perimeter += find_next_sq(a, b, found, grid)
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

    if ((a - 1) >= 0) and grid[a-1][b]:
        next_sqs.append((a-1, b))
    if (b - 1) >= 0 and grid[a][b-1]:
        next_sqs.append((a, b-1))
    if (b < (len(grid[0]) - 1)) and grid[a][b+1]:
        next_sqs.append((a, b+1))
    if (a < (len(grid) - 1)) and grid[a+1][b]:
        next_sqs.append((a+1, b))

    return next_sqs
