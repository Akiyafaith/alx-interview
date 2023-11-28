# Island Perimeter Calculator

## Overview

This Python script calculates the perimeter of an island based on a given grid. The grid represents an island where 0 represents water and 1 represents land. The script follows specific constraints outlined below.

## Constraints

- The grid is rectangular, with its width and height not exceeding 100.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Usage

To use the script, provide the island configuration in the form of a 2D list. The script will then calculate and print the perimeter of the island.

### Example

```python
# Define the island grid
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# Calculate and print the perimeter
print(island_perimeter(grid))
