# rain/person.py

import pygame
import pymunk
from config import WIDTH

class Person:
    def __init__(self, space):
        # Load and scale person image (3x size)
        self.image = pygame.image.load("assets/person.png")
        self.image = pygame.transform.scale(self.image, (240, 300))  # 3x bigger

        # Set up physics body
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = (WIDTH // 2, 450)  # Lowered a bit for new height
        self.rect = self.image.get_rect(center=self.body.position)

        # Collision shape: match image size
        self.shape = pymunk.Poly.create_box(self.body, (180, 270))  # Wide and tall
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

