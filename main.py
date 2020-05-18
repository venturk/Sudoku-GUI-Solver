class SudokuSolver(object):
    def __init__(self, b=None):
        self._board = b
        pass

    def solve(self):
        for i in range(9):  # for each roe
            for j in range(9):  # for each column
                if self._board[i][j] == 0:  # if cell is empty
                    for val in range(1, 10):  # Digits 1-9
                        if self.possible(i, j, val):  # Try every possible digit for current cell
                            self._board[i][j] = val  # Assign current value
                            if self.solve():  # Try solving recursively
                                return True

                            self._board[i][j] = 0  # We couldn't solve with current digit --> Undo assignment

                    return False  # There is no legal digit to assign

        return True  # There are no empty cells!

    def possible(self, row, col, val):
        for r in self._board[row]:  # Search for same value in same row
            if r == val:
                return False

        for i in range(9):  # Search for same value in same column
            if self._board[i][col] == val:
                return False

        row = (row // 3) * 3  # 1st row index of current box
        col = (col // 3) * 3  # 1st column index of current box

        for i in range(3):  # Search for same value in same BOX
            for j in range(3):
                if self._board[row + i][col + j] == val:
                    return False

        return True

    def print_board(self):
        for i, row in enumerate(self._board):
            if not i == 0 and not i % 3:  # New horizontal border
                print("-" * 22)

            for j, val in enumerate(row):
                text = '{}'.format(val)
                if not j == 0 and not j % 3:  # New vertical border
                    text = "| " + text

                print('{}'.format(text), end=" ")  # Print value
            print()  # new line

    def draw_board(self):
        pass


if __name__ == '__main__':
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

    s = SudokuSolver(board)
    s.solve()
    s.print_board()

