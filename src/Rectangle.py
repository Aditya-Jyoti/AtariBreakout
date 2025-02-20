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
        border_colour: str,
        border_width: int = 2,
        border_radius: int = 5,
    ) -> None:
        super().__init__()

        width, height = cells_row * cell_size, cells_col * cell_size

        # Create transparent surface
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

        # Draw filled rectangle with rounded edges
        pygame.draw.rect(
            self.image,
            pygame.Color(colour),
            (0, 0, width, height),
            border_radius=border_radius,
        )

        # Draw border on top
        pygame.draw.rect(
            self.image,
            pygame.Color(border_colour),
            (0, 0, width, height),
            border_width,
            border_radius,
        )

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
