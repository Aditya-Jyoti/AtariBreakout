import pygame


# Inheritable base class for all rectangles in the project
# Handles the creation of a rectangle with a specified colour, position and size
class Rectangle(pygame.sprite.Sprite):
    def __init__(
        self,
        colour: str,
        x: int,
        y: int,
        cells_col: int,
        cells_row: int,
        cell_size: int,
    ) -> None:
        super().__init__()

        self.image = pygame.Surface((cells_col * cell_size, cells_row * cell_size))
        self.image.fill(pygame.Color(colour))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
