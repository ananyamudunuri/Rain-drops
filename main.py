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

    # Create bucket object
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

        # Handle keyboard movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bucket.move("left")
        if keys[pygame.K_RIGHT]:
            bucket.move("right")

        # Rain drop generation
        rain_speed = slider.val
        frame_count += 1
        if frame_count >= (FPS // max(rain_speed, 1)):
            drop = create_drop(space)
            drops.append(drop)
            frame_count = 0

        # Physics step
        space.step(1 / FPS)

        # Draw bucket
        for shape in bucket.get_shapes():
            a = shape.a.rotated(shape.body.angle) + bucket.body.position
            b = shape.b.rotated(shape.body.angle) + bucket.body.position
            pygame.draw.line(screen, (255, 255, 255), a, b, 5)

        # Draw raindrops
        draw_drops(screen, drops)

        # Draw slider
        slider.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
