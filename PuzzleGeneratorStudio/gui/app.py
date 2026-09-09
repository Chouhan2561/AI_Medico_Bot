# ==========================================================
# Puzzle Generator Studio
# Main Application Window
# ==========================================================

import customtkinter as ctk

from gui.header import Header
from gui.sidebar import Sidebar
from gui.statusbar import StatusBar
from gui.themes import load_theme, AppTheme

from gui.home import HomePage

from pages.about import AboutPage
from pages.sudoku import SudokuPage


class PuzzleGeneratorStudio(ctk.CTk):

    def __init__(self):
        super().__init__()

        # --------------------------------------------------
        # Load Theme
        # --------------------------------------------------

        load_theme()

        self.title(AppTheme.TITLE)

        self.geometry(
            f"{AppTheme.WINDOW_WIDTH}x{AppTheme.WINDOW_HEIGHT}"
        )

        self.minsize(
            AppTheme.MIN_WIDTH,
            AppTheme.MIN_HEIGHT
        )

        # --------------------------------------------------
        # Grid Configuration
        # --------------------------------------------------

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(1, weight=1)

        # --------------------------------------------------
        # Header
        # --------------------------------------------------

        self.header = Header(self)

        self.header.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        # --------------------------------------------------
        # Sidebar
        # --------------------------------------------------

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=1,
            column=0,
            sticky="ns"
        )

        # --------------------------------------------------
        # Status Bar
        # --------------------------------------------------

        self.statusbar = StatusBar(self)

        self.statusbar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew"
        )

        # --------------------------------------------------
        # Main Content Area
        # --------------------------------------------------

        self.container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.container.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # --------------------------------------------------
        # Pages Dictionary
        # --------------------------------------------------

        self.pages = {}

        self.create_pages()

        self.show_page("home")

        self.connect_sidebar()

    # ======================================================
    # Create Pages
    # ======================================================

    def create_pages(self):

        self.pages["home"] = HomePage(self.container)

        self.pages["sudoku"] = SudokuPage(self.container)

        self.pages["about"] = AboutPage(self.container)

        for page in self.pages.values():

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

    # ======================================================
    # Show Selected Page
    # ======================================================

    def show_page(self, page_name):

        page = self.pages.get(page_name)

        if page:

            page.tkraise()

            self.statusbar.update_module(
                page_name.title()
            )

            self.statusbar.update_status(
                "Ready"
            )

    # ======================================================
    # Connect Sidebar Buttons
    # ======================================================

    def connect_sidebar(self):

        self.sidebar.home_button.configure(

            command=lambda: self.show_page("home")

        )

        self.sidebar.sudoku_button.configure(

            command=lambda: self.show_page("sudoku")

        )

        self.sidebar.about_button.configure(

            command=lambda: self.show_page("about")

        )