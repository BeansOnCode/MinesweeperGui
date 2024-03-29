"""Contains Game Class"""

from tkinter import Tk

from window import Menu

class Game(Tk):
    def __init__(self):
        """Initialize attributes of game"""
        super().__init__()
        self.title("Minesweeper")
        self.resizable(width=False, height=False)

    def run(self):
        """Start game logic"""
        Menu(self)
        self.mainloop()