# ==========================================================
# Puzzle Generator Studio
# Maze Generator Page
# ==========================================================

import customtkinter as ctk


class MazePage(ctk.CTkFrame):

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
            text="🏰 Maze Generator",
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
Maze Generator will create interactive mazes
using different generation algorithms.

Users will be able to

• Generate Random Mazes

• Choose Maze Size

• Select Difficulty

• Solve Automatically

• Find Shortest Path

• Reset Maze

• Save Maze
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
✔ Recursive Backtracking Algorithm

✔ Depth First Search (DFS)

✔ Prim's Algorithm

✔ Breadth First Search (BFS)

✔ Automatic Solver

✔ Manual Play Mode

✔ Timer

✔ Move Counter

✔ Multiple Maze Sizes

✔ Export Maze as Image
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
            text="Available in Puzzle Generator Studio Version 4.0",
            font=("Segoe UI", 12)
        )

        self.footer.pack(
            pady=20
        )