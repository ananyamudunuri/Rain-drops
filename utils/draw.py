# utils/draw.py

import pygame
from config import DROP_RADIUS

def draw_drops(screen, shapes):
    for shape in shapes:
        if hasattr(shape, 'body'):
            pos = shape.body.position
            pygame.draw.circle(screen, (0, 50, 220), (int(pos.x), int(pos.y)), DROP_RADIUS)
