# main.py

import pygame
import pymunk

from config import WIDTH, HEIGHT, GRAVITY, FPS
from rain.drop import create_drop
from rain.bucket import Bucket
from utils.draw import draw_drops
from utils.slider import Slider
from config import SLIDER_POS, SLIDER_WIDTH, RAIN_SPEED_MIN, RAIN_SPEED_MAX

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rain Simulation")
    clock = pygame.time.Clock()

    # Load background image
    background = pygame.image.load("assets/background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Set up physics
    space = pymunk.Space()
    space.gravity = (0, GRAVITY)

    # Create bucket object with image
    bucket = Bucket(space)

    # Raindrops list
    drops = []

    # Slider for rain speed
    slider = Slider(SLIDER_POS, SLIDER_WIDTH, RAIN_SPEED_MIN, RAIN_SPEED_MAX, 10)
    rain_speed = slider.val
    frame_count = 0

    running = True
    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            slider.handle_event(event)

        # Handle arrow key movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bucket.move("left")
        if keys[pygame.K_RIGHT]:
            bucket.move("right")

        # Spawn raindrops
        rain_speed = slider.val
        frame_count += 1
        if frame_count >= (FPS // max(rain_speed, 1)):
            drop = create_drop(space)
            drops.append(drop)
            frame_count = 0

        # Physics update
        space.step(1 / FPS)

        # Draw drops
        draw_drops(screen, drops)

        # Check if drops hit the bucket
        for drop in drops[:]:
            dx = abs(drop.body.position.x - bucket.body.position.x)
            dy = bucket.body.position.y - drop.body.position.y
            if dx < 35 and 0 < dy < 80:  # Inside bucket zone
                bucket.increase_fill(2)
                space.remove(drop, drop.body)
                drops.remove(drop)

        # Draw bucket (with water fill)
        bucket.draw(screen)

        # Draw rain speed slider
        slider.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
