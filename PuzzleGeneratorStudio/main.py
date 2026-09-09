#Puzzle Generator Studio
#Main Entry Point

from gui.app import PuzzleGeneratorStudio

def main():
    """Launch the Puzzle Generator Studio application."""
    app = PuzzleGeneratorStudio()
    app.mainloop()

if __name__ == "__main__":
    main()