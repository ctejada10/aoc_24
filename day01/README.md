# Day 1: Historian Hysteria

## 📝 Problem Description

The Chief Historian has gone missing, and a group of Senior Historians needs your help to locate him. The historians suspect he visited historically significant locations, and they must reconcile two lists of location IDs from the Chief's office.

### Part One
The historians compare two lists of location IDs. Your task is to compute the **total distance** between the two lists. Pair up the smallest numbers from each list, calculate the absolute difference for each pair, and sum these differences.

### Part Two
After analyzing the lists, the historians suspect many location IDs overlap. Calculate a **similarity score** by determining how many times each number in the left list appears in the right list. For each number, multiply it by the number of occurrences in the right list and sum the results.

## 🔧 Implementation Overview

### Files
- `solution.py`: Contains the implementation of the solution.
- `input.txt`: Placeholder for the input data for this puzzle.

### Key Functions
1. **`parse_file(file_name)`**
   - Reads the input file and parses two lists of integers.
   - Returns the lists sorted for efficient pairing.

2. **`calculate_distance(list1, list2)`**
   - Computes the sum of absolute differences between paired elements in two sorted lists.

3. **`calculate_similarity_score(list1, list2)`**
   - Calculates a similarity score based on the overlap of elements between two lists.

### How to Run
1. Place your input data in the `input.txt` file.
2. Run the script using:
   ```bash
   python solution.py input.txt
   ```

### Example Input
Given two lists:

```
3   4
4   3
2   5
1   3
3   9
3   3
```

**Part One** computes the total distance between paired elements.

**Part Two** computes the similarity score based on overlapping elements.

---

## 📊 Results

### Part One
The total distance between the two lists is computed by summing the absolute differences for each pair.

### Part Two
The similarity score is calculated by summing the weighted overlaps of the numbers in the two lists.

Good luck, and happy coding!
