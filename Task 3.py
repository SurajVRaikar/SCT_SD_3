def is_valid(board, row, col, num):
    """
    Check if placing `num` at board[row][col] is valid.
    """
    for i in range(9):
        # Check the row and column
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Make a tentative assignment

                        if solve_sudoku(board):  # Continue solving recursively
                            return True

                        board[row][col] = 0  # Undo the assignment if it leads to a dead end

                return False  # If no number is valid, backtrack

    return True  # Puzzle solved

def print_board(board):
    """
    Print the Sudoku board.
    """
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku Puzzle:")
    print_board(sudoku_puzzle)

    if solve_sudoku(sudoku_puzzle):
        print("\nSolved Sudoku Puzzle:")
        print_board(sudoku_puzzle)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")
