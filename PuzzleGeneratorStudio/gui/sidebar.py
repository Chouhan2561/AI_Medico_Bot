# ==========================================================
# Puzzle Generator Studio
# Sidebar Component
# ==========================================================

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # --------------------------------------------------
        # Sidebar Configuration
        # --------------------------------------------------

        self.configure(
            width=240,
            corner_radius=0
        )

        self.grid_propagate(False)

        # --------------------------------------------------
        # Sidebar Title
        # --------------------------------------------------

        self.logo_label = ctk.CTkLabel(
            self,
            text="🧩 Puzzle Studio",
            font=("Segoe UI", 22, "bold")
        )

        self.logo_label.pack(
            pady=(25, 10)
        )

        # --------------------------------------------------
        # Navigation Label
        # --------------------------------------------------

        self.navigation_label = ctk.CTkLabel(
            self,
            text="Navigation",
            font=("Segoe UI", 14, "bold")
        )

        self.navigation_label.pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        # --------------------------------------------------
        # Navigation Buttons
        # --------------------------------------------------

        self.home_button = self.create_button(
            "🏠 Home"
        )

        self.sudoku_button = self.create_button(
            "🧩 Sudoku"
        )

        self.word_search_button = self.create_button(
            "🔠 Word Search"
        )

        self.number_puzzle_button = self.create_button(
            "🔢 Number Puzzle"
        )

        self.maze_button = self.create_button(
            "🏰 Maze"
        )

        self.crossword_button = self.create_button(
            "📚 Crossword"
        )

        # --------------------------------------------------
        # Separator
        # --------------------------------------------------

        self.separator = ctk.CTkLabel(
            self,
            text="────────────────────",
            font=("Segoe UI", 12)
        )

        self.separator.pack(
            pady=15
        )

        # --------------------------------------------------
        # Bottom Section
        # --------------------------------------------------

        self.about_button = self.create_button(
            "ℹ About"
        )

        self.exit_button = ctk.CTkButton(
            self,
            text="❌ Exit",
            height=42,
            fg_color="#D32F2F",
            hover_color="#B71C1C",
            command=parent.destroy
        )

        self.exit_button.pack(
            fill="x",
            padx=15,
            pady=6
        )

    # ======================================================
    # Reusable Button Creator
    # ======================================================

    def create_button(self, text):

        button = ctk.CTkButton(
            self,
            text=text,
            height=42,
            anchor="w",
            font=("Segoe UI", 14)
        )

        button.pack(
            fill="x",
            padx=15,
            pady=6
        )

        return button