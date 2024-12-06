from clize import run  # For CLI interface

def read_file(file_name):
    """
    Reads the content of a file.

    Args:
        file_name (str): Path to the input file.

    Returns:
        list[str]: List of lines in the file.
    """
    with open(file_name, 'r') as file:
        return file.readlines()

def parse_grid(lines):
    """
    Parses the grid from the file content.

    Args:
        lines (list[str]): Lines from the file.

    Returns:
        dict: A dictionary where keys are complex numbers representing grid positions
              and values are the corresponding grid characters.
    """
    return {i + j * 1j: c for i, row in enumerate(lines) for j, c in enumerate(row.strip())}

def find_start(grid):
    """
    Finds the starting position in the grid.

    Args:
        grid (dict): The grid dictionary.

    Returns:
        complex: The starting position as a complex number.
    """
    return min(pos for pos, char in grid.items() if char == '^')

def walk(grid, start):
    """
    Simulates a walk on the grid, tracking visited positions and detecting loops.

    Args:
        grid (dict): The grid dictionary.
        start (complex): The starting position.

    Returns:
        tuple[set, bool]: A set of visited positions and a boolean indicating if a loop was detected.
    """
    pos, direction, visited = start, -1, set()

    while pos in grid and (pos, direction) not in visited:
        visited.add((pos, direction))
        if grid.get(pos + direction) == "#":
            direction *= -1j  # Rotate direction counterclockwise
        else:
            pos += direction

    visited_positions = {p for p, _ in visited}
    loop_detected = (pos, direction) in visited
    return visited_positions, loop_detected

def main(file_name='input.txt'):
    """
    Processes the input grid, calculates results for both parts, and prints them.

    Args:
        file_name (str): Path to the input file. Default is 'in.txt'.

    Prints:
        Number of unique visited positions and the count of positions that create loops.
    """
    # Read and parse the grid
    lines = read_file(file_name)
    grid = parse_grid(lines)

    # Find starting position
    start = find_start(grid)

    # Part One: Calculate unique visited positions
    path, _ = walk(grid, start)
    unique_visited = len(path)

    # Part Two: Count positions that create loops when turned into walls
    loop_count = sum(walk(grid | {pos: '#'}, start)[1] for pos in path)

    # Print results
    print(f"Part One: Number of unique visited positions: {unique_visited}")
    print(f"Part Two: Count of positions that create loops: {loop_count}")

if __name__ == "__main__":
    run(main)
