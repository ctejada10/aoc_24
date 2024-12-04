from collections import defaultdict
from clize import run  # For CLI interface

def load_grid(file_name):
    """
    Loads the grid from the input file and constructs a defaultdict.

    Args:
        file_name (str): Path to the input file.

    Returns:
        defaultdict: A grid representation where keys are coordinates (i, j) and values are characters.
    """
    return defaultdict(str) | {
        (i, j): char
        for i, row in enumerate(open(file_name))
        for j, char in enumerate(row.strip())
    }

def count_xmas_lines(grid):
    """
    Counts occurrences of 'XMAS' in straight lines.

    Args:
        grid (dict): The grid of characters.

    Returns:
        int: The count of 'XMAS' occurrences.
    """
    directions = [-1, 0, 1]
    target = list('XMAS'),
    keys = list(grid.keys())
    return sum(
        [grid[i + di * n, j + dj * n] for n in range(4)] in target
        for di in directions for dj in directions for i, j in keys
    )

def count_xmas_crosses(grid):
    """
    Counts occurrences of 'MAS' and 'SAM' in diagonal crosses.

    Args:
        grid (dict): The grid of characters.

    Returns:
        int: The count of 'XMAS' crosses.
    """
    directions = [-1, 0, 1]
    targets = list('MAS'), list('SAM')
    keys = list(grid.keys())
    return sum(
        [grid[i + d, j + d] for d in directions] in targets
        and [grid[i + d, j - d] for d in directions] in targets
        for i, j in keys
    )

def main(file_name='input.txt'):
    """
    Reads the grid from a file, calculates results for both parts of the puzzle, and prints them.

    Args:
        file_name (str): Path to the input file. Default is 'input.txt'.

    Prints:
        Results for Part One and Part Two.
    """
    # Load the grid
    grid = load_grid(file_name)

    # Part One: Count 'XMAS' in straight lines
    part_one_result = count_xmas_lines(grid)

    # Part Two: Count 'MAS'/'SAM' in diagonal crosses
    part_two_result = count_xmas_crosses(grid)

    # Print results
    print(f"Part One: Number of 'XMAS' occurrences in lines: {part_one_result}")
    print(f"Part Two: Number of 'MAS'/'SAM' crosses: {part_two_result}")

if __name__ == "__main__":
    run(main)
