from functools import cmp_to_key
from clize import run  # For CLI interface

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

def compare_pages(x, y, rules):
    """
    Custom comparator to determine the order of two pages based on rules.

    Args:
        x (str): First page.
        y (str): Second page.
        rules (str): Rules defining precedence.

    Returns:
        int: -1 if x should come before y, otherwise 0.
    """
    return -(x + '|' + y in rules)

def sum_middle_pages_for_valid_updates(pages, rules):
    """
    Calculates the sum of middle pages for valid updates.

    Args:
        pages (str): Updates containing page sequences.
        rules (str): Rules defining precedence.

    Returns:
        int: Sum of middle pages for valid updates.
    """
    total = 0

    for update in pages.split():
        page_order = update.split(',')
        sorted_order = sorted(page_order, key=cmp_to_key(lambda x, y: compare_pages(x, y, rules)))
        if page_order == sorted_order:  # Valid update
            total += int(sorted_order[len(sorted_order) // 2])

    return total

def sum_middle_pages_for_invalid_updates(pages, rules):
    """
    Calculates the sum of middle pages for invalid updates.

    Args:
        pages (str): Updates containing page sequences.
        rules (str): Rules defining precedence.

    Returns:
        int: Sum of middle pages for invalid updates.
    """
    total = 0

    for update in pages.split():
        page_order = update.split(',')
        sorted_order = sorted(page_order, key=cmp_to_key(lambda x, y: compare_pages(x, y, rules)))
        if page_order != sorted_order:  # Invalid update
            total += int(sorted_order[len(sorted_order) // 2])

    return total

def main(file_name='input.txt'):
    """
    Reads the file, processes page ordering rules and updates, and prints results.

    Args:
        file_name (str): Path to the input file. Default is 'in.txt'.

    Prints:
        Total sum of middle page numbers for valid and invalid updates.
    """
    # Read file content
    content = read_file(file_name)

    # Split rules and pages
    rules, pages = content.split('\n\n')

    # Calculate sums of middle pages
    valid_sum = sum_middle_pages_for_valid_updates(pages, rules)
    invalid_sum = sum_middle_pages_for_invalid_updates(pages, rules)

    # Print results
    print(f"Sum of middle pages for valid updates: {valid_sum}")
    print(f"Sum of middle pages for invalid updates: {invalid_sum}")

if __name__ == "__main__":
    run(main)
