import pygame
import tomllib

# Load settings from toml file
with open("settings.toml", "rb") as f:
    f = tomllib.load(f)
    settings = f["settings"]
    colours = f["colours"]


# Main game loop
def main(screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()

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

        clock.tick(settings["fps"])
        pygame.display.flip()


# Main runner when script is called
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(settings["caption"])
    pygame.display.set_icon(pygame.image.load(settings["icon"]))

    screen = pygame.display.set_mode(
        (
            settings["num_cells_row"] * settings["cell_size"],
            settings["num_cells_col"] * settings["cell_size"],
        )
    )
    screen.fill(pygame.Color(colours["background"]))

    main(screen)
    pygame.quit()
