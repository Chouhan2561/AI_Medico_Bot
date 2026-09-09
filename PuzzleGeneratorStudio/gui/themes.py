# ==========================================================
# Puzzle Generator Studio
# Theme Configuration
# ==========================================================

import customtkinter as ctk


class AppTheme:
    """
    Centralized theme configuration for the application.
    """

    # ======================================================
    # Appearance
    # ======================================================

    APPEARANCE_MODE = "Dark"          # Dark | Light | System
    COLOR_THEME = "blue"              # blue | green | dark-blue

    # ======================================================
    # Window
    # ======================================================

    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 800

    MIN_WIDTH = 1200
    MIN_HEIGHT = 700

    TITLE = "Puzzle Generator Studio"

    # ======================================================
    # Colors
    # ======================================================

    PRIMARY = "#1F6AA5"
    SECONDARY = "#144870"

    SUCCESS = "#2E7D32"
    WARNING = "#F9A825"
    DANGER = "#C62828"

    BACKGROUND = "#1E1E1E"

    SIDEBAR = "#252526"

    CARD = "#2D2D30"

    HEADER = "#202124"

    STATUSBAR = "#202124"

    TEXT = "#FFFFFF"

    SUBTEXT = "#B0B0B0"

    BORDER = "#3C3C3C"

    HOVER = "#2B88D8"

    # ======================================================
    # Sudoku Colors
    # ======================================================

    SELECTED_CELL = "#1565C0"

    SAME_ROW_COLUMN = "#263238"

    SAME_BOX = "#37474F"

    CORRECT = "#2E7D32"

    WRONG = "#C62828"

    FIXED_NUMBER = "#FFFFFF"

    USER_NUMBER = "#4FC3F7"

    # ======================================================
    # Fonts
    # ======================================================

    TITLE_FONT = ("Segoe UI", 28, "bold")

    HEADING_FONT = ("Segoe UI", 22, "bold")

    SUBHEADING_FONT = ("Segoe UI", 18, "bold")

    NORMAL_FONT = ("Segoe UI", 14)

    SMALL_FONT = ("Segoe UI", 12)

    BUTTON_FONT = ("Segoe UI", 14, "bold")

    # ======================================================
    # Button
    # ======================================================

    BUTTON_HEIGHT = 42

    BUTTON_RADIUS = 8

    # ======================================================
    # Sidebar
    # ======================================================

    SIDEBAR_WIDTH = 240

    # ======================================================
    # Header
    # ======================================================

    HEADER_HEIGHT = 80

    # ======================================================
    # Status Bar
    # ======================================================

    STATUSBAR_HEIGHT = 40

    # ======================================================
    # Sudoku Grid
    # ======================================================

    CELL_SIZE = 55

    GRID_SIZE = 9


# ==========================================================
# Theme Loader
# ==========================================================

def load_theme():
    """
    Load the global application theme.
    """

    ctk.set_appearance_mode(AppTheme.APPEARANCE_MODE)

    ctk.set_default_color_theme(AppTheme.COLOR_THEME)