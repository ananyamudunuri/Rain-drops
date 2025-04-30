# main.py

import pygame
import pymunk

from config import WIDTH, HEIGHT, GRAVITY, FPS
from rain.drop import create_drop
from rain.bucket import create_bucket
from utils.draw import draw_bucket, draw_drops
from utils.slider import Slider
from config import SLIDER_POS, SLIDER_WIDTH, RAIN_SPEED_MIN, RAIN_SPEED_MAX

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rain Simulation")
    clock = pygame.time.Clock()

    # Physics space setup
    space = pymunk.Space()
    space.gravity = (0, GRAVITY)

    # Objects
    bucket = create_bucket(space)
    drops = []

    # Slider
    initial_rain_speed = 10
    slider = Slider(SLIDER_POS, SLIDER_WIDTH, RAIN_SPEED_MIN, RAIN_SPEED_MAX, initial_rain_speed)
    rain_speed = slider.val
    frame_count = 0

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            slider.handle_event(event)

        # Update rain speed from slider
        rain_speed = slider.val
        frame_count += 1
        if frame_count >= (FPS // max(rain_speed, 1)):
            drop = create_drop(space)
            drops.append(drop)
            frame_count = 0

        space.step(1 / FPS)

        # Draw elements
        draw_bucket(screen, bucket)
        draw_drops(screen, drops)
        slider.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
