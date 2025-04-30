# utils/draw.py
import pygame
from config import DROP_RADIUS

def draw_bucket(screen, bucket):
    pygame.draw.line(screen, (255, 255, 255), bucket.a, bucket.b, 10)

def draw_drops(screen, shapes):
    for shape in shapes:
        if isinstance(shape, pygame.Rect): continue
        pos = shape.body.position
        pygame.draw.circle(screen, (0, 150, 255), (int(pos.x), int(pos.y)), DROP_RADIUS)
