# ==========================================================
# Puzzle Generator Studio
# Number Puzzle Page
# ==========================================================

import customtkinter as ctk


class NumberPuzzlePage(ctk.CTkFrame):

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
            text="🔢 Number Puzzle",
            font=("Segoe UI", 30, "bold")
        )

        self.title_label.pack(
            pady=(30, 15)
        )

        # --------------------------------------------------
        # Main Card
        # --------------------------------------------------

        self.card = ctk.CTkFrame(
            self,
            width=850,
            corner_radius=15
        )

        self.card.pack(
            padx=30,
            pady=15,
            fill="both",
            expand=False
        )

        self.coming_label = ctk.CTkLabel(
            self.card,
            text="🚧 COMING SOON",
            font=("Segoe UI", 24, "bold"),
            text_color="orange"
        )

        self.coming_label.pack(
            pady=(25, 10)
        )

        description = """
The Number Puzzle module will provide an
interactive sliding puzzle experience.

Users will be able to

• Shuffle Numbers

• Move Tiles

• Solve Puzzle

• Count Moves

• Track Time

• Restart Puzzle

• Auto Solve
"""

        self.description = ctk.CTkLabel(
            self.card,
            text=description,
            justify="left",
            font=("Segoe UI", 15)
        )

        self.description.pack(
            padx=30,
            pady=(0, 25),
            anchor="w"
        )

        # --------------------------------------------------
        # Planned Features
        # --------------------------------------------------

        self.features = ctk.CTkFrame(
            self,
            width=850,
            corner_radius=15
        )

        self.features.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=False
        )

        self.feature_title = ctk.CTkLabel(
            self.features,
            text="✨ Planned Features",
            font=("Segoe UI", 20, "bold")
        )

        self.feature_title.pack(
            pady=(20, 10)
        )

        feature_text = """
✔ 3 × 3 Sliding Puzzle

✔ 4 × 4 Sliding Puzzle

✔ Random Shuffle

✔ Move Counter

✔ Timer

✔ Auto Solver

✔ Best Score

✔ Game Statistics
"""

        self.feature_label = ctk.CTkLabel(
            self.features,
            text=feature_text,
            justify="left",
            font=("Segoe UI", 15)
        )

        self.feature_label.pack(
            padx=20,
            pady=(0, 20),
            anchor="w"
        )

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        self.footer = ctk.CTkLabel(
            self,
            text="Available in Puzzle Generator Studio Version 3.0",
            font=("Segoe UI", 12)
        )

        self.footer.pack(
            pady=20
        )