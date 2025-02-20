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
        border_colour: str,
        speed: int,
        padding: int,
        display_width: int,
    ) -> None:
        super().__init__(colour, x, y, cells_col, cells_row, cell_size, border_colour)
        self.speed = speed
        self.padding = padding
        self.display_width = display_width
        self.cell_row = cells_row
        self.cell_size = cell_size

    def move_left(self) -> None:
        self.rect.x -= self.speed

        if self.rect.x <= self.padding:
            self.rect.x = self.padding

    def move_right(self) -> None:
        self.rect.x += self.speed
        if self.rect.x >= self.display_width - self.padding - (
            self.cell_row * self.cell_size
        ):
            self.rect.x = (
                self.display_width - (self.cell_row * self.cell_size)
            )
