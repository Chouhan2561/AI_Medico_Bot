# ==========================================================
# Puzzle Generator Studio
# Status Bar Component
# ==========================================================

import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # --------------------------------------------------
        # Status Bar Configuration
        # --------------------------------------------------

        self.configure(
            height=40,
            corner_radius=0
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # --------------------------------------------------
        # Current Module
        # --------------------------------------------------

        self.module_label = ctk.CTkLabel(
            self,
            text="📄 Module : Home",
            font=("Segoe UI", 12)
        )

        self.module_label.grid(
            row=0,
            column=0,
            padx=15,
            pady=8,
            sticky="w"
        )

        # --------------------------------------------------
        # Game Status
        # --------------------------------------------------

        self.status_label = ctk.CTkLabel(
            self,
            text="🟢 Status : Ready",
            font=("Segoe UI", 12)
        )

        self.status_label.grid(
            row=0,
            column=1,
            padx=15,
            pady=8
        )

        # --------------------------------------------------
        # Difficulty
        # --------------------------------------------------

        self.difficulty_label = ctk.CTkLabel(
            self,
            text="🎯 Difficulty : Easy",
            font=("Segoe UI", 12)
        )

        self.difficulty_label.grid(
            row=0,
            column=2,
            padx=15,
            pady=8
        )

        # --------------------------------------------------
        # Version
        # --------------------------------------------------

        self.version_label = ctk.CTkLabel(
            self,
            text="Version 1.0",
            font=("Segoe UI", 12)
        )

        self.version_label.grid(
            row=0,
            column=3,
            padx=15,
            pady=8,
            sticky="e"
        )

    # ======================================================
    # Update Current Module
    # ======================================================

    def update_module(self, module_name):

        self.module_label.configure(
            text=f"📄 Module : {module_name}"
        )

    # ======================================================
    # Update Status
    # ======================================================

    def update_status(self, status):

        self.status_label.configure(
            text=f"🟢 Status : {status}"
        )

    # ======================================================
    # Update Difficulty
    # ======================================================

    def update_difficulty(self, difficulty):

        self.difficulty_label.configure(
            text=f"🎯 Difficulty : {difficulty}"
        )