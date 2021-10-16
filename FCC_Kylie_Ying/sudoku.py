# Solve sudoku using a backtracking technique
# A sudoku game can be represented as an array of lists, with un-guessed squares having a value of -1:

# col: 0   1    2     3   4   5      6    7    8
# [ [  3,  9,  -1,   -1,  5,  -1,   -1,  -1,  -1 ],     <-- row 0
#   [ -1, -1,  -1,    2, -1,  -1,   -1,  -1,  -1 ],     <-- row 1
#   [ -1, -1,  -1,    7,  1,   9,   -1,   8,  -1 ],     <-- row 2
#
#   [ -1,  5,  -1,   -1,  6,   8,    -1,  -1,  -1 ],    <-- row 3
#   [  2, -1,   6,   -1, -1,   3,    -1,  -1,  -1 ],    <-- row 4
#   [ -1, -1,  -1,   -1, -1,  -1,    -1,  -1,   4 ],    <-- row 5
#
#   [ 5, -1,   -1,   -1, -1,  -1,    -1,  -1,  -1 ],    <-- row 6
#   [ 6,  7,   -1,   -1, -1,   5,    -1,   4,  -1 ],    <-- row 7
#   [ 1, -1,    9,   -1, -1,  -1,     2,  -1,  -1 ] ]   <-- row 8

# a.k.a. [[3,9,-1,-1,5,-1,-1,-1,-1],[-1,-1,-1,2,-1,-1,-1,-1,-1],[-1,-1,-1,7,1,9,-1,8,-1],
#         [-1,5,-1,-1,6,8,-1,-1,-1],[2,-1,6,-1,-1,3,-1,-1,-1 ],[-1,-1,-1,-1,-1,-1,-1,-1,4],
#         [5,-1,-1,-1,-1,-1,-1,-1,-1],[6,7,-1,-1,-1,5,-1,4,-1],[1,-1,9,-1,-1,-1,2,-1,-1]]


def find_next_empty(puzzle):
    # Defining the helper function that finds the next row,col on the puzzle that's not filled yet (i.e, == -1)
    # return row, col tuple (or (None, None) if there is none)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # If no spaces in the puzzle are left


def is_valid(puzzle, guess, row, col):
    # Defining a helper function that checks if a guess is valid or not
    # Return True if valid; return False if invalid

    # Checking the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Checking the column:
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Checking the 3x3 square:
    # We want to get where the 3x3 square starts and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    # If we get here, these checks pass
    return True

def solve_sudoku(puzzle):
    # Our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # Return whether a solution exists
    # Mutates puzzle to be the solution (if solution exists)

    # Step 1: choose somewhere on the puzzle to make a guess
    # Make a helper function to find the open spaces on the board:
    row, col = find_next_empty(puzzle)
    # Step 1.1: if there's nowhere left, we're done, because we're only allowed valid inputs
    if row is None:
        return True  # Puzzle solved!

    # Step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1,10):
        # Step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # Step 3.1: if valid, place the guess on the puzzle
            puzzle[row][col] = guess
            # Now recurse using this puzzle
            # Step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # Step 5: if not valid OR if our guess does not solve the puzzle, then we need to backtrack and try a new
        # number
        puzzle[row][col] = -1  # Reset the guess

    # Step 6: if none of the numbers we try work, then the puzzle is unsolveable
    return False

if __name__ == '__main__':
    example_board = [[3,9,-1,-1,5,-1,-1,-1,-1],[-1,-1,-1,2,-1,-1,-1,-1,-1],[-1,-1,-1,7,1,9,-1,8,-1],
                     [-1,5,-1,-1,6,8,-1,-1,-1],[2,-1,6,-1,-1,3,-1,-1,-1 ],[-1,-1,-1,-1,-1,-1,-1,-1,4],
                     [5,-1,-1,-1,-1,-1,-1,-1,-1],[6,7,-1,-1,-1,5,-1,4,-1],[1,-1,9,-1,-1,-1,2,-1,-1]]
    print(solve_sudoku(example_board))
    print(example_board)
