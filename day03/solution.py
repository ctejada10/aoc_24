from clize import run  # For CLI interface
import re

def read_file(file_name):
    """
    Reads the content of a file.

    Args:
        file_name (str): Path to the input file.

    Returns:
        str: Content of the file as a string.
    """
    with open(file_name, 'r') as file:
        return file.read()

def mul(n, m):
    """
    Multiplies two numbers.

    Args:
        n (int): First number.
        m (int): Second number.

    Returns:
        int: Product of n and m.
    """
    return n * m

def main(file_name='input.txt'):
    """
    Processes a corrupted memory log, calculates results for both parts of the puzzle, and prints them.

    Args:
        file_name (str): Path to the input file. Default is 'input.txt'.

    Prints:
        Total sum of results for Part One and Part Two.
    """
    # Read file content
    content = read_file(file_name)

    # Define regex patterns
    mul_pattern = r"mul\(\d{1,3},\s?\d{1,3}\)"  # Matches valid mul operations
    control_pattern = r"do\(\)|don't\(\)"  # Matches control instructions

    # Part One: Sum all valid mul instructions
    matches_part_one = re.findall(mul_pattern, content)
    total_part_one = sum(mul(*map(int, match[4:-1].split(","))) for match in matches_part_one)

    # Part Two: Process matches considering do() and don't()
    matches = re.finditer(f"{mul_pattern}|{control_pattern}", content)
    is_enabled = True  # Multiplications are enabled by default
    total_part_two = 0

    for match in matches:
        instruction = match.group()
        if instruction.startswith("mul("):
            if is_enabled:
                nums = instruction[4:-1].split(",")
                a, b = int(nums[0]), int(nums[1])
                total_part_two += mul(a, b)
        elif instruction == "do()":
            is_enabled = True
        elif instruction == "don't()":
            is_enabled = False

    # Print results for both parts
    print(f"Part One: Total sum of all valid mul results: {total_part_one}")
    print(f"Part Two: Total sum of enabled mul results: {total_part_two}")

if __name__ == "__main__":
    run(main)
