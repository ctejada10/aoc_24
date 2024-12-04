
# Day 4: Ceres Search

## 📝 Problem Description

The Ceres monitoring station's word search puzzle requires finding occurrences of the word "XMAS" in various orientations: horizontally, vertically, diagonally, and in reverse. Additionally, overlapping instances are considered valid.

### Part One

Identify all instances of the word "XMAS" in the grid, regardless of orientation or overlap.

### Part Two

Locate patterns where two instances of "MAS" form an 'X' shape within the grid. Each "MAS" can be oriented forwards or backwards.

## 🔧 Implementation Overview

### Files

- `ceres_search.py`: Contains the implementation of the solution.
- `input.txt`: Contains the word search grid.

### Key Functions

1. **`find_xmas(grid)`**
   - Scans the grid to count all occurrences of "XMAS" in all possible orientations.

2. **`find_x_mas(grid)`**
   - Identifies patterns where two "MAS" sequences form an 'X' shape within the grid.

### How to Run

1. Ensure the word search grid is saved in `input.txt`.
2. Execute the script using:
   ```bash
   python ceres_search.py
   ```

### Example Input

Given the following grid:

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

- **Part One**: Counts all occurrences of "XMAS" in various orientations.
- **Part Two**: Identifies all 'X' shaped patterns formed by "MAS" sequences.

---

## 📊 Results

### Part One

Calculates the total number of "XMAS" occurrences in the grid.

### Part Two

Determines the number of 'X' shaped "MAS" patterns in the grid.

## 🛠️ Solution Inspiration

The solution approach was inspired by a [Reddit comment](https://www.reddit.com/r/adventofcode/comments/1h689qf/2024_day_4_solutions/m0bw4f7/) that suggested using directional vectors to traverse the grid efficiently. By applying this method, the implementation checks each cell in the grid as a potential starting point and explores all possible directions to find the target patterns.

Good luck, and happy coding!
