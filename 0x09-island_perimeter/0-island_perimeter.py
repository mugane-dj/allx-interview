#!/usr/bin/python3
"""
Island perimeter module
"""


def island_perimeter(grid: list[list[int]]) -> int:
    """
    Calculate the perimeter of a 2D matrix

    :param: grid - 2D matrix to calculate perimeter
    :return: perimeter of island (2D matrix)
    """
    n = len(grid)
    m = len(grid[0])
    perimeter = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # edge cell at 1st row or adjacent left cell
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # edge cell at last row or adjacent right cell
                if i == n - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # edge cell at 1st column or adjacent bottom cell
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # edge cell at last column or adjacent top cell
                if j == m - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
