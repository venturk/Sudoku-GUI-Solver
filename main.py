# 43 empty cells
board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


def print_board(board):
    for row in board:
        print(' ', *row)


def possible(board, row, col, val):
    for r in board[row]:  # Search for same value in same row
        if r == val:
            return False

    for i in range(9):  # Search for same value in same column
        if board[i][col] == val:
            return False

    row = (row // 3) * 3  # 1st row index of current box
    col = (col // 3) * 3  # 1st column index of current box

    for i in range(3):  # Search for same value in same BOX
        for j in range(3):
            if board[row + i][col + j] == val:
                return False

    return True


def solve(board):
    for i in range(9):  # for each roe
        for j in range(9):  # for each column
            if board[i][j] == 0:  # if cell is empty
                for val in range(1, 10):  # Digits 1-9
                    if possible(board, i, j, val):  # Try every possible digit for current cell
                        board[i][j] = val  # Assign current value
                        if solve(board):  # Try solving recursively
                            return True

                        board[i][j] = 0  # We couldn't solve with current digit --> Undo assignment

                return False  # There is no legal digit to assign

    return True  # There are no empty cells!


solve(board)
print_board(board)
