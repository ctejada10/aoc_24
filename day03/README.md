
# Day 3: Mull It Over

## 📝 Problem Description

The North Pole Toboggan Rental Shop's computer memory is corrupted, and valid instructions are mixed with invalid characters. Your goal is to extract valid `mul(X,Y)` instructions and calculate their results.

### Part One
Identify and process valid `mul(X,Y)` instructions in the corrupted memory. These instructions multiply two numbers, X and Y, and return their product. Sum the results of all valid instructions.

### Part Two
In addition to `mul(X,Y)` instructions, the program now contains control instructions:
- `do()`: Enables processing of future `mul` instructions.
- `don't()`: Disables processing of future `mul` instructions.

Only the most recent `do()` or `don't()` instruction applies. Initially, all `mul` instructions are enabled. Calculate the sum of results for only the enabled `mul` instructions.

## 🔧 Implementation Overview

### Files
- `script.py`: Contains the implementation of the solution.
- `input.txt`: Placeholder for the input data for this puzzle.

### Key Functions
1. **`read_file(file_name)`**
   - Reads the input file and returns its content as a string.

2. **`mul(n, m)`**
   - Multiplies two numbers and returns the result.

3. **`main(file_name='input.txt')`**
   - Processes the corrupted memory, computes sums for both parts of the puzzle, and prints the results.

### How to Run
1. Place your corrupted memory input in the `input.txt` file.
2. Run the script using:
   ```bash
   python script.py --file_name=input.txt
   ```

### Example Input
Given the following corrupted memory:
```
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
```
**Part One**: Sums the results of valid `mul` instructions.
**Part Two**: Sums the results of enabled `mul` instructions based on the `do()` and `don't()` instructions.

---

## 📊 Results

### Part One
Calculates the sum of all valid `mul` instruction results.

### Part Two
Calculates the sum of enabled `mul` instruction results, considering `do()` and `don't()` instructions.

Good luck, and happy coding!
