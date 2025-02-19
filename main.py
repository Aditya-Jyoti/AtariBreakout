import pygame
import tomllib

from src.Paddle import Paddle

# Load settings from toml file
with open("settings.toml", "rb") as f:
    f = tomllib.load(f)
    settings = f["settings"]
    colours = f["colours"]


# Main game loop
def main(screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()

    # Initialise paddle object in the middle wrt x-axis
    paddle = Paddle(
        x=(
            (
                (
                    (settings["num_cells_row"] * settings["cell_size"])
                    + settings["padding"]
                )
                // 2
            )
            - (
                (
                    (settings["brick_cells_col"] * settings["cell_size"])
                    + settings["padding"]
                )
                // 2
            )
        ),
        y=settings["num_cells_col"] * settings["cell_size"]
        - settings["cell_size"]
        - settings["padding"],
        cell_size=settings["cell_size"],
        cells_col=settings["brick_cells_col"],
        cells_row=settings["brick_cells_row"],
        colour=colours["paddle"],
        speed=settings["paddle_speed"],
    )

    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle)

    running = True
    while running:

        for event in pygame.event.get():

            # Handle quit events
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:

                # Handle quit events
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                    break

        all_sprites.draw(screen)
        clock.tick(settings["fps"])
        pygame.display.flip()


# Main runner when script is called
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(settings["caption"])
    pygame.display.set_icon(pygame.image.load(settings["icon"]))

    screen = pygame.display.set_mode(
        (
            settings["num_cells_row"] * settings["cell_size"] + settings["padding"],
            settings["num_cells_col"] * settings["cell_size"] + settings["padding"],
        )
    )
    screen.fill(pygame.Color(colours["background"]))

    main(screen)
    pygame.quit()
