import pygame
import tomllib

from src.Paddle import Paddle
from utils.level_generator import generate_level

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
                    (
                        settings["brick_cells_row"]
                        * settings["paddle_scale"]
                        * settings["cell_size"]
                    )
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
        cells_row=settings["brick_cells_row"] * settings["paddle_scale"],
        colour=colours["paddle"],
        border_colour=colours["background"],
        speed=settings["paddle_speed"],
        padding=settings["padding"],
        display_width=settings["num_cells_row"] * settings["cell_size"]
    )

    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle)

    bricks = generate_level(
        num_cells_row=settings["num_cells_row"],
        brick_cells_col=settings["brick_cells_col"],
        brick_cells_row=settings["brick_cells_row"],
        cell_size=settings["cell_size"],
        single_hit_brick_colour=colours["single_hit_brick"],
        double_hit_brick_colour=colours["double_hit_brick"],
        triple_hit_brick_colour=colours["triple_hit_brick"],
        padding=settings["padding"],
        border_colour=colours["background"],
    )

    all_sprites.add(bricks)

    running = True
    while running:

        screen.fill(pygame.Color(colours["background"]))

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
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            paddle.move_right()

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
