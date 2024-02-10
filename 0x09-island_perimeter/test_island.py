#!/usr/bin/python3
"""Unnittest for island perimeter function"""
import unittest
island_perimeter = __import__("0-island_perimeter").island_perimeter


class PerimeterTest(unittest.TestCase):
    """ Unittest class for island perimeter function"""

    def test_zero_perimeter(self):
        grid_1 = []
        grid_2 = [[]]
        grid_3 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        grid_4 = [[0], [0], [0]]
        self.assertEqual(island_perimeter(grid_1), 0)
        self.assertEqual(island_perimeter(grid_2), 0)
        self.assertEqual(island_perimeter(grid_3), 0)
        self.assertEqual(island_perimeter(grid_4), 0)

    def test_single_island(self):
        grid_5 = [[1]]
        grid_6 = [[1, 0]]
        self.assertEqual(island_perimeter(grid_5), 4)
        self.assertEqual(island_perimeter(grid_6), 4)

    def test_connected_islands(self):
        grid_7 = [
            [0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]
        ]
        grid_8 = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(island_perimeter(grid_7), 16)
        self.assertEqual(island_perimeter(grid_8), 12)
