from src.Rectangle import Rectangle

import pygame


class Brick(Rectangle):
    def __init__(
        self,
        colour: str,
        x: int,
        y: int,
        cells_col: int,
        cells_row: int,
        cell_size: int,
        border_colour: str,
        strength: int = 1,
    ) -> None:
        super().__init__(colour, x, y, cells_col, cells_row, cell_size, border_colour)
        self.strength = strength
