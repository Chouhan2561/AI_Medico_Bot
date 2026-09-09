# Puzzle Generator Studio
# Sudoku Difficulty 
class SudokuDifficulty:
    """
    Sudoku Difficulty Configuration.
    Defines how many cells are removed from a completed Sudoku board.
    """
    EASY=35
    MEDIUM=45
    HARD=55
    EXPERT=60
    
# Get Difficulty
    @staticmethod
    def get_removed_cells(level):
        """
        Returns the number of cells to remove according to difficulty.
        """
        difficulty=level.lower()
        if difficulty=="easy":
            return SudokuDifficulty.EASY
        elif difficulty=="medium":
            return SudokuDifficulty.MEDIUM
        elif difficulty=="hard":
            return SudokuDifficulty.HARD
        elif difficulty=="expert":
            return SudokuDifficulty.EXPERT
        return SudokuDifficulty.MEDIUM
    
# Get Difficulty Name
    @staticmethod
    def get_levels():
       return [
           "Easy",
           "Medium",
           "Hard",
           "Expert"
       ]