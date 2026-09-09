# ==========================================================
# Puzzle Generator Studio
# Sudoku Page
# ==========================================================

import customtkinter as ctk

from sudoku.generator import SudokuGenerator
from sudoku.solver import SudokuSolver
from sudoku.validator import SudokuValidator
from sudoku.difficulty import SudokuDifficulty
from sudoku.timer import GameTimer


class SudokuPage(ctk.CTkFrame):
    """
    Sudoku Game Page
    """

    def __init__(self, parent):

        super().__init__(parent)

        # --------------------------------------------------
        # Sudoku Engine
        # --------------------------------------------------

        self.generator = SudokuGenerator()
        self.solver = SudokuSolver()
        self.validator = SudokuValidator()
        self.timer_engine = GameTimer()

        # --------------------------------------------------
        # Game Data
        # --------------------------------------------------

        self.current_puzzle = None
        self.current_solution = None
        self.original_puzzle = None

        self.cells = []

        self.mistake_count = 0
        self.move_count = 0

        # --------------------------------------------------
        # Window Layout
        # --------------------------------------------------

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # --------------------------------------------------
        # Build GUI
        # --------------------------------------------------

        self.create_left_panel()
        self.create_board()

        # --------------------------------------------------
        # Start Timer
        # --------------------------------------------------

        self.update_timer()

    # ======================================================
    # Left Panel
    # ======================================================

    def create_left_panel(self):

        self.left_frame = ctk.CTkFrame(
            self,
            width=280,
            corner_radius=15
        )

        self.left_frame.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="ns"
        )

        self.left_frame.grid_propagate(False)

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        title = ctk.CTkLabel(
            self.left_frame,
            text="🧩 Sudoku",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            pady=(20, 15)
        )

        # --------------------------------------------------
        # Difficulty
        # --------------------------------------------------

        difficulty_title = ctk.CTkLabel(
            self.left_frame,
            text="Difficulty",
            font=("Segoe UI", 16, "bold")
        )

        difficulty_title.pack(
            pady=(10, 5)
        )

        self.difficulty = ctk.CTkOptionMenu(
            self.left_frame,
            values=SudokuDifficulty.get_levels(),
            command=self.change_difficulty
        )

        self.difficulty.set("Easy")

        self.difficulty.pack(
            padx=20,
            fill="x"
        )

        # --------------------------------------------------
        # Generate Puzzle
        # --------------------------------------------------

        self.generate_button = ctk.CTkButton(
            self.left_frame,
            text="🎲 Generate Puzzle",
            height=42,
            command=self.generate_puzzle
        )

        self.generate_button.pack(
            padx=20,
            pady=(20, 8),
            fill="x"
        )

        # --------------------------------------------------
        # Solve Puzzle
        # --------------------------------------------------

        self.solve_button = ctk.CTkButton(
            self.left_frame,
            text="🧠 Solve Puzzle",
            height=42,
            command=self.solve_puzzle
        )

        self.solve_button.pack(
            padx=20,
            pady=8,
            fill="x"
        )

        # --------------------------------------------------
        # Check Solution
        # --------------------------------------------------

        self.check_button = ctk.CTkButton(
            self.left_frame,
            text="✅ Check Solution",
            height=42,
            command=self.check_solution
        )

        self.check_button.pack(
            padx=20,
            pady=8,
            fill="x"
        )

        # --------------------------------------------------
        # Hint
        # --------------------------------------------------

        self.hint_button = ctk.CTkButton(
            self.left_frame,
            text="💡 Hint",
            height=42,
            command=self.show_hint
        )

        self.hint_button.pack(
            padx=20,
            pady=8,
            fill="x"
        )

        # --------------------------------------------------
        # Reset
        # --------------------------------------------------

        self.reset_button = ctk.CTkButton(
            self.left_frame,
            text="🔄 Reset",
            height=42,
            command=self.reset_board
        )

        self.reset_button.pack(
            padx=20,
            pady=8,
            fill="x"
        )

        # --------------------------------------------------
        # New Game
        # --------------------------------------------------

        self.new_game_button = ctk.CTkButton(
            self.left_frame,
            text="🆕 New Game",
            height=42,
            command=self.new_game
        )

        self.new_game_button.pack(
            padx=20,
            pady=8,
            fill="x"
        )
        # --------------------------------------------------
        # Statistics
        # --------------------------------------------------

        self.statistics_frame = ctk.CTkFrame(
            self.left_frame,
            corner_radius=10
        )

        self.statistics_frame.pack(
            padx=20,
            pady=(25, 10),
            fill="x"
        )

        statistics_title = ctk.CTkLabel(
            self.statistics_frame,
            text="📊 Game Statistics",
            font=("Segoe UI", 18, "bold")
        )

        statistics_title.pack(
            pady=(15, 10)
        )

        self.timer_label = ctk.CTkLabel(
            self.statistics_frame,
            text="⏱ Time : 00:00",
            font=("Segoe UI", 14)
        )

        self.timer_label.pack(
            pady=5
        )

        self.moves_label = ctk.CTkLabel(
            self.statistics_frame,
            text="🎯 Moves : 0",
            font=("Segoe UI", 14)
        )

        self.moves_label.pack(
            pady=5
        )

        self.mistake_label = ctk.CTkLabel(
            self.statistics_frame,
            text="❌ Mistakes : 0",
            font=("Segoe UI", 14)
        )

        self.mistake_label.pack(
            pady=5
        )

        self.status_label = ctk.CTkLabel(
            self.statistics_frame,
            text="🟢 Ready",
            font=("Segoe UI", 14)
        )

        self.status_label.pack(
            pady=(5, 15)
        )

    # ======================================================
    # Sudoku Board
    # ======================================================

    def create_board(self):

        self.board_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.board_frame.grid(
            row=0,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.board_frame.grid_columnconfigure(
            0,
            weight=1
        )

        title = ctk.CTkLabel(
            self.board_frame,
            text="Sudoku Board",
            font=("Segoe UI", 28, "bold")
        )

        title.pack(
            pady=(20, 20)
        )

        self.grid_frame = ctk.CTkFrame(
            self.board_frame,
            fg_color="transparent"
        )

        self.grid_frame.pack(
            pady=10
        )

        self.cells = []

        for row in range(9):

            row_cells = []

            for col in range(9):

                padx = (2, 2)
                pady = (2, 2)

                if col % 3 == 0:
                    padx = (6, 2)

                if row % 3 == 0:
                    pady = (6, 2)

                if col == 8:
                    padx = (2, 6)

                if row == 8:
                    pady = (2, 6)

                cell = ctk.CTkEntry(
                    self.grid_frame,
                    width=48,
                    height=48,
                    justify="center",
                    font=("Consolas", 20, "bold")
                )

                cell.grid(
                    row=row,
                    column=col,
                    padx=padx,
                    pady=pady
                )

                row_cells.append(cell)

            self.cells.append(row_cells)

        self.info_label = ctk.CTkLabel(
            self.board_frame,
            text="Choose a difficulty and click Generate Puzzle.",
            font=("Segoe UI", 14)
        )

        self.info_label.pack(
            pady=(15, 20)
        )
        # ======================================================
    # Change Difficulty
    # ======================================================

    def change_difficulty(self, value):
        """
        Update the selected difficulty.
        """

        self.selected_difficulty = value

        self.status_label.configure(
            text=f"🟢 Difficulty : {value}"
        )

    # ======================================================
    # Generate Puzzle
    # ======================================================

    def generate_puzzle(self):
        """
        Generate a new Sudoku puzzle.
        """

        difficulty = self.difficulty.get()

        cells = SudokuDifficulty.get_removed_cells(
            difficulty
        )

        puzzle, solution = self.generator.generate_puzzle(
            cells
        )

        self.current_puzzle = puzzle

        self.current_solution = solution

        self.original_puzzle = [

            row.copy()

            for row in puzzle

        ]

        self.display_board()

        self.mistake_count = 0

        self.move_count = 0

        self.timer_engine.reset()

        self.timer_engine.start()

        self.status_label.configure(
            text="🟢 Puzzle Generated"
        )

        self.info_label.configure(
            text=f"{difficulty} Puzzle Generated Successfully"
        )

    # ======================================================
    # Display Puzzle
    # ======================================================

    def display_board(self):
        """
        Display the current Sudoku puzzle.
        """

        if self.current_puzzle is None:
            return

        for row in range(9):

            for col in range(9):

                cell = self.cells[row][col]

                cell.configure(
                    state="normal"
                )

                cell.delete(
                    0,
                    "end"
                )

                value = self.current_puzzle[row][col]

                if value != 0:

                    cell.insert(
                        0,
                        str(value)
                    )

                    cell.configure(
                        state="disabled"
                    )

                else:

                    cell.configure(
                        state="normal"
                    )
        # ======================================================
    # Solve Puzzle
    # ======================================================

    def solve_puzzle(self):
        """
        Solve the current Sudoku puzzle.
        """

        if self.current_solution is None:

            self.status_label.configure(
                text="🔴 Generate a puzzle first."
            )

            return

        for row in range(9):

            for col in range(9):

                value = self.current_solution[row][col]

                cell = self.cells[row][col]

                cell.configure(state="normal")

                cell.delete(0, "end")

                cell.insert(0, str(value))

                cell.configure(
                    state="disabled"
                )

        self.status_label.configure(
            text="🟢 Puzzle Solved"
        )

        self.info_label.configure(
            text="Sudoku solved successfully."
        )

        self.timer_engine.stop()

    # ======================================================
    # Check Solution
    # ======================================================

    def check_solution(self):
        """
        Compare user entries with the solution.
        """

        if self.current_solution is None:

            self.status_label.configure(
                text="🔴 Generate a puzzle first."
            )

            return

        mistakes = 0

        for row in range(9):

            for col in range(9):

                cell = self.cells[row][col]

                # Skip original fixed cells
                if self.original_puzzle[row][col] != 0:
                    continue

                value = cell.get().strip()

                if value == "":
                    continue

                try:

                    value = int(value)

                except ValueError:

                    mistakes += 1

                    cell.configure(
                        border_color="red"
                    )

                    continue

                if value != self.current_solution[row][col]:

                    mistakes += 1

                    cell.configure(
                        border_color="red"
                    )

                else:

                    cell.configure(
                        border_color="green"
                    )

        self.mistake_count = mistakes

        self.mistake_label.configure(
            text=f"❌ Mistakes : {mistakes}"
        )

        if mistakes == 0:

            self.status_label.configure(
                text="🟢 Excellent! No mistakes found."
            )

            self.info_label.configure(
                text="Puzzle is correct."
            )

        else:

            self.status_label.configure(
                text=f"🟠 {mistakes} mistake(s) found."
            )

            self.info_label.configure(
                text="Incorrect cells are highlighted."
            )
        # ======================================================
    # Show Hint
    # ======================================================

    def show_hint(self):
        """
        Reveal one correct value in an empty cell.
        """

        if self.current_solution is None:

            self.status_label.configure(
                text="🔴 Generate a puzzle first."
            )

            return

        for row in range(9):

            for col in range(9):

                if self.original_puzzle[row][col] != 0:
                    continue

                cell = self.cells[row][col]

                value = cell.get().strip()

                if value == "":

                    answer = self.current_solution[row][col]

                    cell.delete(0, "end")

                    cell.insert(0, str(answer))

                    cell.configure(
                        border_color="green"
                    )

                    self.status_label.configure(
                        text="💡 Hint Used"
                    )

                    self.info_label.configure(
                        text=f"Hint added at Row {row+1}, Column {col+1}"
                    )

                    return

        self.status_label.configure(
            text="🟢 No empty cells available."
        )

    # ======================================================
    # Reset Board
    # ======================================================

    def reset_board(self):
        """
        Restore the original generated puzzle.
        """

        if self.original_puzzle is None:

            self.status_label.configure(
                text="🔴 Generate a puzzle first."
            )

            return

        self.current_puzzle = [

            row.copy()

            for row in self.original_puzzle

        ]

        self.display_board()

        self.mistake_count = 0

        self.move_count = 0

        self.mistake_label.configure(
            text="❌ Mistakes : 0"
        )

        self.moves_label.configure(
            text="🎯 Moves : 0"
        )

        self.status_label.configure(
            text="🟢 Puzzle Reset"
        )

        self.info_label.configure(
            text="Puzzle restored to its original state."
        )
        # ======================================================
    # New Game
    # ======================================================

    def new_game(self):
        """
        Start a completely new game.
        """

        self.generate_puzzle()

    # ======================================================
    # Update Timer
    # ======================================================

    def update_timer(self):
        """
        Update timer every second.
        """

        if self.timer_engine.is_running():

            self.timer_label.configure(
                text=f"⏱ Time : {self.timer_engine.formatted_time()}"
            )

        self.after(
            1000,
            self.update_timer
        )

    # ======================================================
    # Clear Board
    # ======================================================

    def clear_board(self):
        """
        Clears all cells.
        """

        for row in range(9):

            for col in range(9):

                cell = self.cells[row][col]

                cell.configure(
                    state="normal",
                    border_color=("gray70", "gray40")
                )

                cell.delete(0, "end")

    # ======================================================
    # Read User Board
    # ======================================================

    def get_current_board(self):
        """
        Returns the current board entered by the user.
        """

        board = []

        for row in range(9):

            board_row = []

            for col in range(9):

                value = self.cells[row][col].get().strip()

                if value == "":

                    board_row.append(0)

                else:

                    try:

                        board_row.append(int(value))

                    except ValueError:

                        board_row.append(0)

            board.append(board_row)

        return board

    # ======================================================
    # Lock Original Cells
    # ======================================================

    def lock_original_cells(self):
        """
        Disable the original puzzle cells.
        """

        if self.original_puzzle is None:
            return

        for row in range(9):

            for col in range(9):

                cell = self.cells[row][col]

                if self.original_puzzle[row][col] != 0:

                    cell.configure(
                        state="disabled"
                    )

                else:

                    cell.configure(
                        state="normal"
                    )

    # ======================================================
    # Unlock Board
    # ======================================================

    def unlock_board(self):
        """
        Enable every cell.
        """

        for row in range(9):

            for col in range(9):

                self.cells[row][col].configure(
                    state="normal"
                )

    # ======================================================
    # Update Move Counter
    # ======================================================

    def update_moves(self):

        self.move_count += 1

        self.moves_label.configure(

            text=f"🎯 Moves : {self.move_count}"

        )

    # ======================================================
    # Reset Statistics
    # ======================================================

    def reset_statistics(self):

        self.move_count = 0

        self.mistake_count = 0

        self.moves_label.configure(

            text="🎯 Moves : 0"

        )

        self.mistake_label.configure(

            text="❌ Mistakes : 0"

        )

        self.status_label.configure(

            text="🟢 Ready"

        )

    # ======================================================
    # End Game
    # ======================================================

    def finish_game(self):

        self.timer_engine.stop()

        self.status_label.configure(

            text="🎉 Congratulations!"

        )

        self.info_label.configure(

            text="Sudoku Completed Successfully."

        )