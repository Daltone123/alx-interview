#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Start with 4 edges
                perimeter += 4
                # Subtract edges for adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Check below
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Check right
                    perimeter -= 1

    return perimeter
