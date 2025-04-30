# utils/draw.py

import pygame
from config import DROP_RADIUS

def draw_drops(screen, shapes):
    for shape in shapes:
        if hasattr(shape, 'body'):
            pos = shape.body.position
            # Use shape.radius (can shrink dynamically)
            radius = int(getattr(shape, "custom_radius", DROP_RADIUS))
            if radius > 0:
                pygame.draw.circle(screen, (0, 100, 255), (int(pos.x), int(pos.y)), radius)

