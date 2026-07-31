"""
LeetCode 36 - Valid Sudoku

Determine whether a partially filled 9 x 9 Sudoku board is valid. Each row,
column, and 3 x 3 box must contain digits 1-9 at most once. A dot represents an
empty cell. The board does not need to be solvable.
"""

# region Inputs
board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
expected1 = True

board2 = [row[:] for row in board1]
board2[0][0] = "8"
expected2 = False

board3 = [["."] * 9 for _ in range(9)]
expected3 = True
# endregion


# region Methods
def is_valid_sudoku(board):
    pass


# endregion


# region Calls
result1 = is_valid_sudoku(board1)
result2 = is_valid_sudoku(board2)
result3 = is_valid_sudoku(board3)
# endregion


# region Print
print("Case 1:", result1, "Expected:", expected1)
print("Case 2:", result2, "Expected:", expected2)
print("Case 3:", result3, "Expected:", expected3)
# endregion
