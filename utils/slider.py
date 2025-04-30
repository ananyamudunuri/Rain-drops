# utils/slider.py
import pygame
from config import *

class Slider:
    def __init__(self, pos, width, min_val, max_val, initial_val):
        self.x, self.y = pos
        self.width = width
        self.min_val = min_val
        self.max_val = max_val
        self.val = initial_val
        self.knob_x = self._val_to_pos(self.val)
        self.dragging = False

    def _val_to_pos(self, val):
        return int(self.x + ((val - self.min_val) / (self.max_val - self.min_val)) * self.width)

    def _pos_to_val(self, x):
        return int(self.min_val + ((x - self.x) / self.width) * (self.max_val - self.min_val))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if abs(event.pos[0] - self.knob_x) <= SLIDER_KNOB_RADIUS and abs(event.pos[1] - self.y) <= 20:
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.knob_x = max(self.x, min(event.pos[0], self.x + self.width))
            self.val = self._pos_to_val(self.knob_x)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, SLIDER_HEIGHT))
        pygame.draw.circle(screen, (255, 0, 0), (self.knob_x, self.y + SLIDER_HEIGHT // 2), SLIDER_KNOB_RADIUS)
        font = pygame.font.SysFont(None, 20)
        label = font.render(f"Rain Speed: {self.val} drops/sec", True, (255, 255, 255))
        screen.blit(label, (self.x, self.y - 25))
