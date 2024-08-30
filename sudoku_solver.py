def is_valid_move(grid, row, column, number):
    
    # Checks if number is already in a row
    for x in range(9):   
        if grid[row][x] == number:
            return False
    
    # Checks if number is already in a column
    for x in range(9): 
        if grid[x][column] == number:
            return False
    
    # Find starting index for subgrids of 3x3 squares
    corner_row = row - row % 3
    corner_column = column - column % 3
    
    # Checks if number is in 3x3 square subgrids
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_column + y] == number:
                return False

    return True

def solve(grid, row, column):

    # If we reach the end of a row (column index 9), move to the next row
    if column == 9:
        if row == 8: # If we're at the last row and the last column, the puzzle is solved
            return True
        row += 1 # Move to the next row
        column = 0 # Start from the first column of the next row

    # If the current cell is already filled (non-zero), move to the next cell
    if grid[row][column] > 0:
        return solve(grid, row, column + 1)
    
    # Try placing numbers 1 to 9 in empty cell
    for num in range(1, 10):
        if is_valid_move(grid, row, column, num):
            grid[row][column] = num
            # Recursively solve the rest of the grid
            if solve(grid, row, column + 1):
                return True
        
        # If 'num' does not lead to a solution, reset the cell and go to the next number
        grid[row][column] = 0
    
    return False

# Grid with some cells filled in
# Empty cells represented as 0 
grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]

# Output the solved sudoku
# Start solving from the top-left corner
if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution for this sudoku")
