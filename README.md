# sudoku-puzzle-solver

# Sudoku Solver

This project is a Python implementation of a Sudoku puzzle solver using the backtracking algorithm. The solver takes a partially filled 9x9 Sudoku grid and completes it according to the standard Sudoku rules.

## Features

- Solves any valid 9x9 Sudoku puzzle.
- Uses a backtracking algorithm to find the solution.
- Includes input validation to ensure that the solution adheres to Sudoku rules.

## Usage

1. The Sudoku puzzle is represented as a 9x9 grid in the `grid` variable within `sudoku_solver.py`. Empty cells are denoted by `0`.
2. Modify the `grid` variable in the `sudoku_solver.py` file with your Sudoku puzzle.
3. Run the solver:
    ```bash
    python sudoku_solver.py
    ```
4. The solution will be printed in the terminal. If no solution is possible, a message will be displayed.