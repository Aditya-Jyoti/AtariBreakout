import pygame
import tomllib

# Load settings from toml file
with open("settings.toml", "rb") as f:
    settings = tomllib.load(f)["settings"]

# Main runner when script is called
if __name__ == "__main__":
    pygame.init()
