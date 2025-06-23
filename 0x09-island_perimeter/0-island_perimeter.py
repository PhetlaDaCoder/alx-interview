#!/usr/bin/python3
"""Island perimeter finder function."""


def island_perimeter(grid):
    """Returns perimeter of island.
     Grid represnts land  by 1 and water by 0.
     Args:
        grid(list): A list on intergers representing the island.
    Return:
        perimeter of island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for n in range(height):
        for m in range(width):
            if grid[n][m] == 1:
                size += 1
                if (m > 0 and grid[n][m - 1] == 1):
                    edges += 1
                if (n > 0 and grid[n - 1][m] == 1):
                    edges += 1
    return size * 4 - edges * 2
