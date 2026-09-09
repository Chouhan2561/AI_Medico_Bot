# ==========================================================
# Puzzle Generator Studio
# Home Page
# ==========================================================

import customtkinter as ctk


class HomePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # --------------------------------------------------
        # Page Configuration
        # --------------------------------------------------

        self.configure(
            fg_color="transparent"
        )

        self.grid_columnconfigure((0, 1), weight=1)

        # ==================================================
        # Welcome Section
        # ==================================================

        self.title_label = ctk.CTkLabel(
            self,
            text="Welcome to Puzzle Generator Studio",
            font=("Segoe UI", 28, "bold")
        )

        self.title_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(30, 10)
        )

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Develop, Play and Solve Professional Logic Puzzles",
            font=("Segoe UI", 16)
        )

        self.subtitle_label.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(0, 30)
        )

        # ==================================================
        # Available Puzzle Card
        # ==================================================

        self.available_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.available_frame.grid(
            row=2,
            column=0,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.available_title = ctk.CTkLabel(
            self.available_frame,
            text="🟢 Available Puzzle",
            font=("Segoe UI", 20, "bold")
        )

        self.available_title.pack(pady=(20, 15))

        self.sudoku_label = ctk.CTkLabel(
            self.available_frame,
            text="""
🧩 Sudoku Generator

✔ Generate Puzzle

✔ Solve Puzzle

✔ Check Solution

✔ Multiple Difficulty Levels
""",
            justify="left",
            font=("Segoe UI", 14)
        )

        self.sudoku_label.pack(
            padx=20,
            pady=(0, 20)
        )

        # ==================================================
        # Upcoming Puzzle Card
        # ==================================================

        self.upcoming_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.upcoming_frame.grid(
            row=2,
            column=1,
            padx=20,
            pady=20,
            sticky="nsew"
        )

        self.upcoming_title = ctk.CTkLabel(
            self.upcoming_frame,
            text="🚀 Upcoming Modules",
            font=("Segoe UI", 20, "bold")
        )

        self.upcoming_title.pack(
            pady=(20, 15)
        )

        self.upcoming_label = ctk.CTkLabel(
            self.upcoming_frame,
            text="""
🔠 Word Search

🏰 Maze Generator

📚 Crossword Puzzle

🔢 Number Puzzle

🎯 More Coming Soon...
""",
            justify="left",
            font=("Segoe UI", 14)
        )

        self.upcoming_label.pack(
            padx=20,
            pady=(0, 20)
        )

        # ==================================================
        # Features Section
        # ==================================================

        self.feature_frame = ctk.CTkFrame(
            self,
            corner_radius=15
        )

        self.feature_frame.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=20,
            pady=20,
            sticky="ew"
        )

        self.feature_title = ctk.CTkLabel(
            self.feature_frame,
            text="✨ Features",
            font=("Segoe UI", 20, "bold")
        )

        self.feature_title.pack(
            pady=(20, 15)
        )

        self.feature_label = ctk.CTkLabel(
            self.feature_frame,
            text="""
✔ Modern CustomTkinter Interface

✔ Interactive Sudoku Board

✔ Puzzle Solver

✔ Hint System

✔ Timer

✔ Difficulty Levels

✔ Statistics Dashboard

✔ Save & Load Games
""",
            justify="left",
            font=("Segoe UI", 14)
        )

        self.feature_label.pack(
            padx=20,
            pady=(0, 20)
        )

        # ==================================================
        # Footer
        # ==================================================

        self.footer = ctk.CTkLabel(
            self,
            text="Puzzle Generator Studio • Version 1.0 • Python + CustomTkinter",
            font=("Segoe UI", 12)
        )

        self.footer.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(10, 20)
        )