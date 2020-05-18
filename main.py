import tkinter as tk
import copy


class SudokuSolver(object):
    def __init__(self):
        self.__board = None
        self.__is_gui = None
        self.__root = None
        self.__labels = None

    def gui_solver(self, board):
        self.__is_gui = True
        self.__board = copy.deepcopy(board)
        self.__root = tk.Tk()
        self.__labels = []

        self.__draw_board()
        self.__root.after(1, self.__solve)
        self.__root.mainloop()

    def cmd_solver(self, board):
        self.__is_gui = False
        self.__board = copy.deepcopy(board)

        self.__solve()
        self.print_board(self.__board)

    def __solve(self):
        for i in range(9):  # for each row
            for j in range(9):  # for each column
                if self.__board[i][j] == 0:  # if cell is empty
                    for val in range(1, 10):  # Digits 1-9
                        if self.__possible(i, j, val):  # Try every possible (i.e legal) digit for current cell
                            self.__board[i][j] = val  # Assign current value
                            if self.__is_gui:
                                self.__update_cell(i, j, val)

                            if self.__solve():  # Try solving recursively
                                return True

                            self.__board[i][j] = 0  # We couldn't solve with current digit --> Undo assignment
                            if self.__is_gui:
                                self.__update_cell(i, j, 0)
                    return False  # There is no legal digit to assign

        return True  # There are no empty cells! HOORAY!

    def __possible(self, row, col, val):
        for r in self.__board[row]:  # Search for same value in same row
            if r == val:
                return False

        for i in range(9):  # Search for same value in same column
            if self.__board[i][col] == val:
                return False

        row = (row // 3) * 3  # 1st row index of current box
        col = (col // 3) * 3  # 1st column index of current box

        for i in range(3):  # Search for same value in same BOX
            for j in range(3):
                if self.__board[row + i][col + j] == val:
                    return False

        return True

    @staticmethod
    def print_board(b):
        if b is None:
            return

        for i, row in enumerate(b):
            if not i == 0 and not i % 3:  # New horizontal border
                print("-" * 22)

            for j, val in enumerate(row):
                text = '{}'.format(val)
                if not j == 0 and not j % 3:  # New vertical border
                    text = "| " + text

                print('{}'.format(text), end=" ")  # Print value
            print()  # new line
        print()

    def __update_cell(self, row, col, value):
        pass

    def __draw_board(self):
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

    s = SudokuSolver()
    s.print_board(board)  # Before solving
    s.cmd_solver(board)  # After solving
    s.gui_solver(board)  # GUI solving with animation of backtracking
