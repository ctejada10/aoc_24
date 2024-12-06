
# Day 6: Guard Gallivant

## 📝 Problem Description

The Historians are searching for the Chief in the North Pole prototype suit manufacturing lab, but a guard is patrolling the area. Your task is to predict the guard's patrol route and determine specific positions in the lab based on their movement rules.

### Part One

Predict the guard's patrol route through the grid and calculate the number of distinct positions the guard visits before leaving the mapped area.

### Part Two

Determine the number of positions where a new obstruction could be placed to cause the guard to get stuck in a loop, making the lab safe to search. The new obstruction cannot be placed at the guard's starting position.

---

## 🔧 Implementation Overview

### Files

- `guard_gallivant.py`: Python script implementing the solution.
- `input.txt`: Input file containing the grid map of the lab.

### Key Functions

1. **`read_file(file_name)`**
   - Reads the input file and returns the list of lines.

2. **`parse_grid(lines)`**
   - Converts the input lines into a dictionary representation of the grid.
   - Each position in the grid is represented as a complex number (`row + col * 1j`), making it easier to perform directional calculations.

3. **`find_start(grid)`**
   - Locates the starting position of the guard in the grid based on the `^` character.

4. **`walk(grid, start)`**
   - Simulates the guard's movement across the grid.
   - Tracks all visited positions and detects loops based on the guard's position and direction.
   - Returns the set of visited positions and whether a loop was detected.

5. **`main(file_name)`**
   - Orchestrates the process:
     - Parses the grid.
     - Identifies the starting position.
     - Computes the number of unique positions visited (Part One).
     - Determines the number of positions that cause a loop when turned into obstacles (Part Two).

---

## 🛠️ Solution Approach

The solution uses a dictionary-based grid representation where each cell is indexed by a complex number (`row + col * 1j`). This representation simplifies directional movement calculations:
- **Direction Handling**:
  - Directions are represented as complex numbers (`1j` for up, `-1j` for down, `1` for right, `-1` for left).
  - If an obstacle (`#`) is directly ahead, the guard turns right (90-degree clockwise rotation achieved by multiplying the direction by `-1j`).
  - Otherwise, the guard steps forward in the current direction.

- **Simulation**:
  - The `walk` function tracks the guard's movement using a set of visited positions. It also keeps track of the guard's direction and detects loops when a position is revisited with the same direction.

- **Part One**:
  - Simulates the guard's full patrol route and counts the number of distinct positions visited.

- **Part Two**:
  - Tests each position in the guard's patrol path as a potential new obstacle. For each potential obstacle, the function simulates the patrol again to check if it creates a loop.

### How to Run

1. Place the input file (`input.txt`) in the same directory as the script.
2. Run the script using:
   ```bash
   python guard_gallivant.py
   ```

### Example Input

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

### Example Output

- **Part One**: Number of distinct positions visited by the guard.
- **Part Two**: Number of positions that cause the guard to get stuck in a loop.

---

## 📊 Results

### Part One

- Calculates the total number of distinct positions visited by the guard.

### Part Two

- Determines the number of potential positions for an obstruction that creates a loop.

Good luck, and happy coding!
