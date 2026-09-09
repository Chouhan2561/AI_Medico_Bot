# ==========================================================
# Puzzle Generator Studio
# Sudoku Validator
# ==========================================================


class SudokuValidator:
    """
    Validates Sudoku moves.

    Responsibilities
    ----------------
    • Check Row
    • Check Column
    • Check 3x3 Box
    • Validate Number Placement
    • Check Completed Board
    """

    BOARD_SIZE = 9
    BOX_SIZE = 3

    # ======================================================
    # Check Row
    # ======================================================

    @staticmethod
    def is_row_valid(board, row, number):
        """
        Returns False if the number already exists
        in the given row.
        """

        return number not in board[row]

    # ======================================================
    # Check Column
    # ======================================================

    @staticmethod
    def is_column_valid(board, col, number):
        """
        Returns False if the number already exists
        in the given column.
        """

        for row in range(SudokuValidator.BOARD_SIZE):

            if board[row][col] == number:
                return False

        return True

    # ======================================================
    # Check 3x3 Box
    # ======================================================

    @staticmethod
    def is_box_valid(board, row, col, number):
        """
        Returns False if the number already exists
        inside the corresponding 3x3 box.
        """

        start_row = row - row % SudokuValidator.BOX_SIZE
        start_col = col - col % SudokuValidator.BOX_SIZE

        for r in range(start_row, start_row + 3):

            for c in range(start_col, start_col + 3):

                if board[r][c] == number:
                    return False

        return True

    # ======================================================
    # Validate Move
    # ======================================================

    @staticmethod
    def is_valid_move(board, row, col, number):
        """
        Returns True if a number can be placed
        in the specified position.
        """

        return (

            SudokuValidator.is_row_valid(
                board,
                row,
                number
            )

            and

            SudokuValidator.is_column_valid(
                board,
                col,
                number
            )

            and

            SudokuValidator.is_box_valid(
                board,
                row,
                col,
                number
            )

        )

    # ======================================================
    # Find Empty Cell
    # ======================================================

    @staticmethod
    def find_empty_cell(board):
        """
        Returns first empty cell.

        Returns:
            (row, col)

        If board is full

            Returns None
        """

        for row in range(9):

            for col in range(9):

                if board[row][col] == 0:
                    return row, col

        return None

    # ======================================================
    # Check Board Complete
    # ======================================================

    @staticmethod
    def is_complete(board):
        """
        Returns True if no empty cells exist.
        """

        return SudokuValidator.find_empty_cell(board) is None