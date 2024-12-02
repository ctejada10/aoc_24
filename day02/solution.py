from clize import run  # For CLI interface

def parse_file(file_name):
    """
    Parses a text file and extracts lists of integers for each report.

    Args:
        file_name (str): Path to the input file.

    Returns:
        list: A list of reports, where each report is a list of integers.
    """
    with open(file_name, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def is_safe(report):
    """
    Checks if a report is safe based on the initial criteria.

    A report is safe if:
    - Levels are either all increasing or all decreasing.
    - Adjacent levels differ by at least 1 and at most 3.

    Args:
        report (list): List of integers representing a report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    differences_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    return differences_valid and (increasing or decreasing)

def is_safe_with_dampener(report):
    """
    Checks if a report can be made safe by removing a single level.

    Args:
        report (list): List of integers representing a report.

    Returns:
        bool: True if the report can be made safe, False otherwise.
    """
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

def main(file_name):
    """
    Reads data from a file, computes the number of safe reports, and prints the results.

    Args:
        file_name (str): Path to the input file.
    """
    reports = parse_file(file_name)
    
    # Count reports that are safe without using the dampener
    undamped_safe = sum(is_safe(report) for report in reports)
    
    # Count reports that can be made safe using the dampener
    damped_safe = sum(is_safe_with_dampener(report) for report in reports if not is_safe(report))
    
    # Total safe reports
    total_safe = undamped_safe + damped_safe

    print(f"Safe reports (without dampener): {undamped_safe}")
    print(f"Safe reports (with dampener): {damped_safe}")
    print(f"Total safe reports: {total_safe}")

if __name__ == "__main__":
    run(main)
