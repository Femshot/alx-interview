#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    grid2 = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    grid3 = [[1]]
    grid4 = [[1, 0]]
    grid5 = [[]]
    grid6 = []
    grid7 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    print(island_perimeter(grid))
    print(island_perimeter(grid2))
    print(island_perimeter(grid3))
    print(island_perimeter(grid4))
    print(island_perimeter(grid5))
    print(island_perimeter(grid6))
    print(island_perimeter(grid7))
