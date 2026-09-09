# ==========================================================
# Puzzle Generator Studio
# Crossword Puzzle Page
# ==========================================================

import customtkinter as ctk


class CrosswordPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(
            fg_color="transparent"
        )

        self.create_widgets()

    # ======================================================
    # Create Widgets
    # ======================================================

    def create_widgets(self):

        # --------------------------------------------------
        # Page Title
        # --------------------------------------------------

        self.title_label = ctk.CTkLabel(
            self,
            text="📚 Crossword Puzzle",
            font=("Segoe UI", 30, "bold")
        )

        self.title_label.pack(
            pady=(30, 15)
        )

        # --------------------------------------------------
        # Main Information Card
        # --------------------------------------------------

        self.main_card = ctk.CTkFrame(
            self,
            width=850,
            corner_radius=15
        )

        self.main_card.pack(
            padx=30,
            pady=15,
            fill="both",
            expand=False
        )

        self.status_label = ctk.CTkLabel(
            self.main_card,
            text="🚧 COMING SOON",
            font=("Segoe UI", 24, "bold"),
            text_color="orange"
        )

        self.status_label.pack(
            pady=(25, 10)
        )

        description = """
The Crossword Puzzle module will generate
interactive crossword puzzles with automatic
word placement.

Users will be able to

• Generate Crossword Puzzles

• Select Difficulty

• Reveal Hints

• Check Answers

• Auto Solve

• Save Crossword

• Print Crossword
"""

        self.description_label = ctk.CTkLabel(
            self.main_card,
            text=description,
            justify="left",
            anchor="w",
            font=("Segoe UI", 15)
        )

        self.description_label.pack(
            padx=30,
            pady=(0, 25),
            anchor="w"
        )

        # --------------------------------------------------
        # Planned Features
        # --------------------------------------------------

        self.features_card = ctk.CTkFrame(
            self,
            width=850,
            corner_radius=15
        )

        self.features_card.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=False
        )

        self.features_title = ctk.CTkLabel(
            self.features_card,
            text="✨ Planned Features",
            font=("Segoe UI", 20, "bold")
        )

        self.features_title.pack(
            pady=(20, 10)
        )

        features = """
✔ Automatic Crossword Generator

✔ Across & Down Clues

✔ Hint System

✔ Reveal Letter

✔ Reveal Word

✔ Multiple Difficulty Levels

✔ Category Based Crosswords

✔ Random Puzzle Generator

✔ Timer

✔ Score Tracking

✔ Solution Viewer

✔ Export & Print Puzzle
"""

        self.features_label = ctk.CTkLabel(
            self.features_card,
            text=features,
            justify="left",
            anchor="w",
            font=("Segoe UI", 15)
        )

        self.features_label.pack(
            padx=20,
            pady=(0, 20),
            anchor="w"
        )

        # --------------------------------------------------
        # Future Algorithms
        # --------------------------------------------------

        self.algorithm_card = ctk.CTkFrame(
            self,
            width=850,
            corner_radius=15
        )

        self.algorithm_card.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=False
        )

        self.algorithm_title = ctk.CTkLabel(
            self.algorithm_card,
            text="🧠 Crossword Algorithms",
            font=("Segoe UI", 20, "bold")
        )

        self.algorithm_title.pack(
            pady=(20, 10)
        )

        algorithms = """
• Word Placement Algorithm

• Grid Optimization

• Backtracking Algorithm

• Crossword Validation

• Random Clue Selection

• Difficulty Optimization
"""

        self.algorithm_label = ctk.CTkLabel(
            self.algorithm_card,
            text=algorithms,
            justify="left",
            anchor="w",
            font=("Segoe UI", 15)
        )

        self.algorithm_label.pack(
            padx=20,
            pady=(0, 20),
            anchor="w"
        )

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        self.footer = ctk.CTkLabel(
            self,
            text="Available in Puzzle Generator Studio Version 5.0",
            font=("Segoe UI", 12)
        )

        self.footer.pack(
            pady=20
        )