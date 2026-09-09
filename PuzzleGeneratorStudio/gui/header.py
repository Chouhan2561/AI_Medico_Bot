# ==========================================================
# Puzzle Generator Studio
# Header Component
# ==========================================================

import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # --------------------------------------------------
        # Header Configuration
        # --------------------------------------------------

        self.configure(
            height=80,
            corner_radius=0
        )

        self.grid_columnconfigure(0, weight=1)

        # --------------------------------------------------
        # Main Title
        # --------------------------------------------------

        self.title_label = ctk.CTkLabel(
            self,
            text="🧩 Puzzle Generator Studio",
            font=("Segoe UI", 28, "bold")
        )

        self.title_label.pack(
            pady=(10, 0)
        )

        # --------------------------------------------------
        # Subtitle
        # --------------------------------------------------

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Professional Puzzle Development Platform",
            font=("Segoe UI", 14)
        )

        self.subtitle_label.pack()

        # --------------------------------------------------
        # Version
        # --------------------------------------------------

        self.version_label = ctk.CTkLabel(
            self,
            text="Version 1.0",
            font=("Segoe UI", 12)
        )

        self.version_label.pack(
            pady=(0, 10)
        )