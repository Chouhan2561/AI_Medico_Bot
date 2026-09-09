
#Puzzle Generator Studio 
# Sudoku Board Class

from copy import deepcopy
class SudokuBoard:
    """
    Represents a 9X9 Sudoku board.
    Responsibilities
    ---------------
    Store the Sudoku board.
    Create an empty board.
    Reset the board.
    Get and set cell values.
    Print the board (Debugging).
    Clone the board.
    """
    BOARD_SIZE = 9
    BOX_SIZE = 3
    def __init__(self):
        """
        Create a new empty Sudoku board.
        """
        self.board=self.create_empty_board()
        
# Create Empty Board
    def create_empty_board(self):
        """
        Create a 9 X 9 board filled with zeros.
        """
        return[
            [0 for _ in range(self.BOARD_SIZE)] 
            for _ in range(self.BOARD_SIZE)
        ]
        
# Reset Board
    def reset_board(self):
        """
        Clears the Sudoku board.
        """
        self.board=self.create_empty_board()
        
# Get Complete Board
    def get_board(self):
        """
        Returns the complete Sudoku board.
        """
        return self.board
    
# Replace Board
    def set_board(self, new_board):
        """
        Replace the current board.
        """
        self.board=deepcopy(new_board)
        
# Get Cell Value
    def get_cell(self, row, col):
        """
        Returns value of a particular cell.
        """
        return self.board[row][col]
    
# Update Cell
    def set_cell(self, row, col, value):
        """
        Updates a particular cell.
        """
        self.board[row][col]=value 
        
# Check Empty Cell
    def is_empty(self, row, col):
        """
        Returns True if the cell is empty.
        """
        return self.board[row][col]==0
    
# Clone Board
    def clone(self):
        """
        Returns a deep copy of the Sudoku board.
        """
        return deepcopy(self.board)
    
# Print Board
    def display(self):
        """
        Display the Sudoku board in console.
        Useful for debugging.
        """
        print("-"*31)
        for row in range(self.BOARD_SIZE):
            if row % 3==0 and row !=0:
                print("-"*31)
            for col in range(self.BOARD_SIZE):
                if col % 3==0:
                    print("|", end="")
                value=self.board[row][col]
                if value==0:
                    print(". ", end="")
                else:
                    print(f"{value}  ", end="")
            print("|")
        print("-"*31)
        
# Board Dimensions
    def rows(self):
        return self.BOARD_SIZE
    def columns(self):
        return self.BOARD_SIZE
                    
            