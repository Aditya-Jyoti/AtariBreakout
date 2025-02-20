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
        self.max_strength = strength  # Store initial strength for reference
        self.original_colour = pygame.Color(colour)  # Store original colour
        self.border_colour = pygame.Color(border_colour)  # Store border colour

    def hit(self):
        """Reduce brick strength and darken colour before removing."""
        if self.strength > 1:
            self.strength -= 1
            self._darken_colour()  # Darken before breaking
        else:
            self.kill()  # Remove from sprite group

    def _darken_colour(self):
        """Reduce brightness of the brick color while keeping rounded corners."""
        darken_factor = self.strength / self.max_strength  # Gradual darkening
        new_colour = (
            max(0, int(self.original_colour.r * darken_factor)),
            max(0, int(self.original_colour.g * darken_factor)),
            max(0, int(self.original_colour.b * darken_factor)),
        )

        # Re-draw rectangle to maintain rounded corners
        self.image.fill((0, 0, 0, 0))  # Clear with transparency
        pygame.draw.rect(
            self.image,
            new_colour,
            (0, 0, self.rect.width, self.rect.height),
            border_radius=5,  # Maintain rounded corners
        )
        pygame.draw.rect(
            self.image,
            self.border_colour,
            (0, 0, self.rect.width, self.rect.height),
            2,  # Border width
            border_radius=5,  # Maintain rounded border
        )
