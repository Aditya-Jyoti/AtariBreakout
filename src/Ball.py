import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, colour, x, y, radius, speed, display_width, display_height):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.Color(colour), (radius, radius), radius)

        self.rect = self.image.get_rect()
        self.radius = radius
        self.speed = speed
        self.display_width = display_width
        self.display_height = display_height

        # Ball starts stuck to the paddle
        self.rect.center = (x, y)
        self.attached_to_paddle = True
        self.speed_x = 0
        self.speed_y = 0

    def attach_to_paddle(self, paddle):
        self.rect.midbottom = (paddle.rect.centerx, paddle.rect.top - 1)

    def launch(self):
        self.attached_to_paddle = False
        angle = random.uniform(-45, 45)  # Random initial angle
        self.speed_x = self.speed * (angle / 45)  # Scale based on angle
        self.speed_y = -self.speed  # Always move upward

    def update(self, paddle, bricks):
        if self.attached_to_paddle:
            self.attach_to_paddle(paddle)
            return  # Stop movement until launched

        # Move the ball
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off left/right walls
        if self.rect.left <= 0 or self.rect.right >= self.display_width:
            self.speed_x *= -1

        # Bounce off top wall
        if self.rect.top <= 0:
            self.speed_y *= -1

        # Paddle collision
        if self.rect.colliderect(paddle.rect) and self.speed_y > 0:
            self.speed_y *= -1
            offset = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
            self.speed_x += offset * 3  # Adjust angle based on where it hits

        # Filter out "killed" bricks
        active_bricks = [brick for brick in bricks if brick.alive()]

        # Brick collisions (only check alive bricks)
        for brick in active_bricks:
            if self.rect.colliderect(brick.rect):
                brick.hit()  # Reduce brick strength or remove it
                self.speed_y *= -1  # Bounce off
                break  # Avoid multiple collisions in one frame

        # If ball falls below the screen, reset it
        if self.rect.bottom >= self.display_height:
            self.attached_to_paddle = True
            self.attach_to_paddle(paddle)
