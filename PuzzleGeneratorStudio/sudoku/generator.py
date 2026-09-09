import random
from sudoku.solver import SudokuSolver
from sudoku.validator import SudokuValidator
class SudokuGenerator:
    """
    Sudoku Puzzle Generator.
    Responsibilities
    ----------------
    ~Generate Full Sudoku
    ~Remove Cells
    ~Generate Playable Puzzle
    """
    BOARD_SIZE=9
    def __init__(self):
        self.solver=SudokuSolver()
        self.validator=SudokuValidator()
        
# Create Empty Board 
    def create_empty_board(self):
        return [
            [0 for _ in range(self.BOARD_SIZE)] 
            for _ in range(self.BOARD_SIZE)
        ]
        
# Generate Complete Sudoku
    def generate_complete_board(self):
        """
        Generates a complete Sudoku board.
        """
        board=self.create_empty_board()
        self.fill_board(board)
        return board
    
# Fill Board Recursively
    def fill_board(self,board):
        empty=self.validator.find_empty_cell(board)
        if empty is None:
            return True
        row,col=empty
        numbers=list(range(1,10))
        random.shuffle(numbers)
        for number in numbers:
            if self.validator.is_valid_move(
                board,
                row,
                col,
                number
            ):
                board[row][col]=number
                if self.fill_board(board):
                    return True
                board[row][col]=0
        return False
    
# Remove Cells
    def remove_cells(self,board,cells_to_remove):
        puzzle= [
            row.copy()
            for row in board
        ]
        removed=0
        while removed<cells_to_remove:
            row=random.randint(0,8)
            col=random.randint(0,8)
            if puzzle[row][col]!=0:
                puzzle[row][col]=0
                removed+=1
        return puzzle
    
# Generate Puzzle
    def generate_puzzle(self,cells_to_remove=40):
        completed_board=self.generate_complete_board()
        puzzle=self.remove_cells(
            completed_board,
            cells_to_remove
            )
        return puzzle,completed_board