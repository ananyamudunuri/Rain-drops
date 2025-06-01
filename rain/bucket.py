# rain/bucket.py

import pygame
import pymunk
from config import WIDTH

class Bucket:
    def __init__(self, space):
        # Load and scale the bucket image
        self.image = pygame.image.load("assets/bucket.png")
        self.image = pygame.transform.scale(self.image, (120, 100))  # Adjust size as needed

        # Set up physics body
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = (WIDTH // 2, 500)
        self.rect = self.image.get_rect(center=self.body.position)

        # Create a rectangular collision box for the bucket
        self.shape = pymunk.Poly.create_box(self.body, (90, 60))  # hitbox width/height
        self.shape.elasticity = 0.8
        space.add(self.body, self.shape)

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

    def get_shape(self):
        return self.shape
