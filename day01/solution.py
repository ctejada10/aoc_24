from clize import run  # For CLI interface

def parse_file(file_name):
    """
    Parses a text file and extracts two lists of integers.
    Each line in the file should contain two integers separated by whitespace.

    Args:
        file_name (str): Path to the input file.

    Returns:
        tuple: Two sorted lists of integers.
    """
    with open(file_name, 'r') as file:
        l1, l2 = zip(*(map(int, line.split()) for line in file))
    return sorted(l1), sorted(l2)

def calculate_distance(list1, list2):
    """
    Calculates the sum of absolute differences between corresponding elements of two lists.

    Args:
        list1 (list): First list of integers.
        list2 (list): Second list of integers.

    Returns:
        int: Sum of absolute differences.
    """
    return sum(abs(a - b) for a, b in zip(list1, list2))

def calculate_similarity_score(list1, list2):
    """
    Calculates a similarity score based on the product of matching elements between two lists.

    Args:
        list1 (list): First list of integers.
        list2 (list): Second list of integers.

    Returns:
        int: Similarity score.
    """
    list2_counts = {num: list2.count(num) for num in set(list2)}
    return sum(num * list2_counts.get(num, 0) for num in list1)

def main(file_name):
    """
    Reads data from a file, computes metrics, and prints the results.

    Args:
        file_name (str): Path to the input file.
    """
    list1, list2 = parse_file(file_name)
    distance = calculate_distance(list1, list2)
    similarity_score = calculate_similarity_score(list1, list2)
    
    print(f"Distance: {distance}")
    print(f"Similarity Score: {similarity_score}")

if __name__ == "__main__":
    run(main)
