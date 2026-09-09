# ==========================================================
# Puzzle Generator Studio
# About Page
# ==========================================================

import customtkinter as ctk


class AboutPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # --------------------------------------------------
        # Page Configuration
        # --------------------------------------------------

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
            text="ℹ About Puzzle Generator Studio",
            font=("Segoe UI", 30, "bold")
        )

        self.title_label.pack(
            pady=(30, 15)
        )

        # --------------------------------------------------
        # Description Frame
        # --------------------------------------------------

        self.description_frame = ctk.CTkFrame(
            self,
            width=900,
            corner_radius=15
        )

        self.description_frame.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=False
        )

        # --------------------------------------------------
        # Description
        # --------------------------------------------------

        description = """
Puzzle Generator Studio is a professional desktop application
developed using Python and CustomTkinter.

The goal of this software is to provide an interactive platform
for learning, generating and solving different logic-based puzzles.

Current Module
• Sudoku Generator

Upcoming Modules
• Word Search Generator
• Number Puzzle
• Maze Generator
• Crossword Generator

This project is designed for educational purposes and follows
professional software engineering practices.
"""

        self.description_label = ctk.CTkLabel(
            self.description_frame,
            text=description,
            justify="left",
            anchor="w",
            font=("Segoe UI", 15)
        )

        self.description_label.pack(
            padx=25,
            pady=25,
            anchor="w"
        )

        # --------------------------------------------------
        # Technology Frame
        # --------------------------------------------------

        self.tech_frame = ctk.CTkFrame(
            self,
            width=900,
            corner_radius=15
        )

        self.tech_frame.pack(
            padx=30,
            pady=20,
            fill="both",
            expand=False
        )

        self.tech_title = ctk.CTkLabel(
            self.tech_frame,
            text="🛠 Technologies Used",
            font=("Segoe UI", 20, "bold")
        )

        self.tech_title.pack(
            pady=(20, 10)
        )

        technologies = """
✔ Python 3

✔ CustomTkinter

✔ Object-Oriented Programming

✔ Modular Project Structure

✔ Backtracking Algorithm (Sudoku)

✔ Professional GUI Design
"""

        self.tech_label = ctk.CTkLabel(
            self.tech_frame,
            text=technologies,
            justify="left",
            font=("Segoe UI", 15)
        )

        self.tech_label.pack(
            padx=20,
            pady=(0, 20),
            anchor="w"
        )

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        self.footer = ctk.CTkLabel(
            self,
            text="Puzzle Generator Studio • Version 1.0",
            font=("Segoe UI", 12)
        )

        self.footer.pack(
            pady=20
        )