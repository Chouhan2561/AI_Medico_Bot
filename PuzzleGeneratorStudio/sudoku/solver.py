# Puzzle Generator Studio
# Sudoku Solver
from sudoku.validator import SudokuValidator
class SudokuSolver:
    """
    Sudoku Solver using the Backtracking Algorithm.
    Responsibilities
    ----------------
    ~ Solve Sudoku Puzzle
    ~ Find Empty Cells
    ~ Validates Moves
    ~ Fill the Board
    """
    
# Constructor
    def __init__(self):
        """
        Initialize Sudoku Solver.
        """
        self.validator=SudokuValidator()
        
# Solve Sudoku
    def solve(self,board):
        """
        Solve the Sudoku puzzle using backtracking.
        Parameters
        ----------
        board : list[list[int]]
        Returns
        -------
        bool
            True  --> Puzzle Solved
            False --> No Solution Exists
        """
        
# Find  an Empty Cell
        empty_cell=self.validator.find_empty_cell(board)
        
# Puzzle Completed
        if empty_cell is None:
            return True
        row,col=empty_cell
        
# Try Numbers 1-9

