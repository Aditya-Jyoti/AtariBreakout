from src.Rectangle import Rectangle


class Paddle(Rectangle):
    def __init__(
        self,
        colour: str,
        x: int,
        y: int,
        cells_col: int,
        cells_row: int,
        cell_size: int,
        speed: int,
    ) -> None:
        super().__init__(colour, x, y, cells_col, cells_row, cell_size)
        self.speed = speed
