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

    # TODO search for same value in same BOX
    return True


def solve(board):
    pass

