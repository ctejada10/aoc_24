
# Day 5: Print Queue

## 📝 Problem Description

The North Pole printing department is overwhelmed with updates for the sleigh launch safety manuals. Each update must follow a strict ordering of pages defined by specific precedence rules. The task involves identifying which updates are already correctly ordered and reordering the remaining updates to follow the rules.

### Part One

Identify the updates that are already correctly ordered based on the provided rules. For each correctly-ordered update, find the middle page number. Sum these middle page numbers to get the result for Part One.

### Part Two

For updates that are not correctly ordered, reorder them based on the rules. Then, calculate the middle page number for each reordered update and sum these values to obtain the result for Part Two.

---

## 🔧 Implementation Overview

### Files

- `solution.py`: Python script implementing the solution.
- `input.txt`: Input file containing the page ordering rules and updates.

### Key Functions

1. **`read_file(file_name)`**
   - Reads the input file and separates it into rules and updates.

2. **`compare_pages(x, y, rules)`**
   - Custom comparator function that determines the precedence of two pages based on the rules.

3. **`sum_middle_pages_for_valid_updates(pages, rules)`**
   - Calculates the sum of middle pages for updates already in the correct order.

4. **`sum_middle_pages_for_invalid_updates(pages, rules)`**
   - Reorders invalid updates and calculates the sum of their middle pages.

5. **`main(file_name)`**
   - Orchestrates the process: parses input, evaluates valid and invalid updates, and prints the results for both parts.

---

## 🛠️ Solution Approach

The solution leverages Python's `functools.cmp_to_key` to create a custom sorting function based on the precedence rules. Each update is processed independently:
- For valid updates, the script directly evaluates their middle page.
- For invalid updates, the script reorders the pages before computing the middle page.

This efficient approach ensures the program handles large inputs within reasonable time limits.

### How to Run

1. Place the input file (`input.txt`) in the same directory as the script.
2. Run the script using:
   ```bash
   python print_queue.py
   ```

### Example Input

The input consists of two sections:
1. **Rules**: Define the precedence between pages (e.g., `47|53` means 47 must precede 53).
2. **Updates**: Lists of pages in each update (e.g., `75,47,61,53,29`).

Example:
```
47|53
97|13
...
75,47,61,53,29
97,61,53,29,13
...
```

---

## 📊 Results

### Part One

- Identifies updates that are already in the correct order.
- Sums the middle page numbers of these updates.

### Part Two

- Reorders incorrectly ordered updates based on the rules.
- Sums the middle page numbers of the reordered updates.

---

## 🛠️ Solution Inspiration

The solution design was inspired by the task of sorting with custom precedence, often discussed in algorithmic communities. Specifically, the use of `cmp_to_key` was inspired by a [Reddit comment](https://www.reddit.com/r/adventofcode/comments/1h71eyz/2024_day_5_solutions/m0i09b0/) that highlighted its applicability for handling custom comparisons efficiently.

Good luck, and happy coding!
