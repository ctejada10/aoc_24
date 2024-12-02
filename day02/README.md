
# Day 2: Red-Nosed Reports

## 📝 Problem Description

The engineers at the Red-Nosed reactor need your help analyzing unusual data reports to determine which reports are safe.

### Part One
A report is considered **safe** if:
1. The levels in the report are either all increasing or all decreasing.
2. Any two adjacent levels differ by at least 1 and at most 3.

### Part Two
The engineers introduce the **Problem Dampener**, which allows the reactor safety systems to tolerate a single bad level. A report is considered safe if removing a single level makes it safe.

### Example Input
The input consists of multiple reports, one per line, where each report is a list of numbers separated by spaces:

```
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
```

**Part One Output:**
- Safe reports: `7 6 4 2 1` and `1 3 6 7 9`.

**Part Two Output:**
- Additional safe reports: `1 3 2 4 5` and `8 6 4 4 1`.

## 🔧 Implementation Overview

### Files
- `script.py`: Contains the implementation of the solution.
- `input.txt`: Placeholder for the input data for this puzzle.

### Key Functions
1. **`parse_file(file_name)`**
   - Reads the input file and parses reports into a list of lists of integers.

2. **`is_safe(report)`**
   - Checks if a report meets the safety criteria.

3. **`is_safe_with_dampener(report)`**
   - Checks if a report can be made safe by removing a single level.

4. **`main(file_name='input.txt')`**
   - Parses the file and computes the number of safe reports with and without the Problem Dampener.

### How to Run
1. Place your input data in the `input.txt` file.
2. Run the script using:
   ```bash
   python script.py --file_name=input.txt
   ```

### Example Output
For the example input provided above, the script will output:
- The total number of safe reports based on Part One criteria.
- The total number of safe reports considering the Problem Dampener.

---

## 📊 Results

### Part One
The number of reports that are safe without using the Problem Dampener.

### Part Two
The number of reports that are safe with the Problem Dampener.

Good luck, and happy coding!
