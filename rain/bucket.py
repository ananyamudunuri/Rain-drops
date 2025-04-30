import pygame
import pymunk
from config import WIDTH

class Bucket:
    def __init__(self, space):
        self.image = pygame.image.load("assets/bucket.png")
        self.image = pygame.transform.scale(self.image, (80, 80))

        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = (WIDTH // 2, 520)

        self.rect = self.image.get_rect(center=self.body.position)

        # Define a static hitbox shape for physics (bottom of bucket)
        self.shape = pymunk.Segment(self.body, (-40, 0), (40, 0), 5)
        self.shape.elasticity = 0.8
        space.add(self.body, self.shape)

        self.fill_level = 0  # Track how full the bucket is

    def move(self, direction):
        speed = 300
        x, y = self.body.position
        if direction == "left":
            x = max(40, x - speed / 60)
        elif direction == "right":
            x = min(WIDTH - 40, x + speed / 60)
        self.body.position = (x, y)
        self.rect.center = self.body.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # Draw water fill inside bucket
        if self.fill_level > 0:
            fill_height = min(self.fill_level, 70)
            water_rect = pygame.Rect(
                self.rect.left + 10,
                self.rect.bottom - fill_height - 10,
                self.rect.width - 20,
                fill_height
            )
            pygame.draw.rect(screen, (0, 100, 255), water_rect)

    def get_shape(self):
        return self.shape

    def increase_fill(self, amount):
        self.fill_level += amount

