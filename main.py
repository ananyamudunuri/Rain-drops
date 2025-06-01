# main.py

import pygame
import pymunk

from config import WIDTH, HEIGHT, GRAVITY, FPS
from rain.drop import create_drop
from rain.bucket import Bucket  # ✅ updated
from utils.draw import draw_drops
from utils.slider import Slider
from config import SLIDER_POS, SLIDER_WIDTH, RAIN_SPEED_MIN, RAIN_SPEED_MAX

def main():
    pygame.init()
    pygame.mixer.init()

    # 🎵 Play background music automatically
    pygame.mixer.music.load("assets/light-rain.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rain Simulation")
    clock = pygame.time.Clock()

    # Load background image
    background = pygame.image.load("assets/background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Set up physics space
    space = pymunk.Space()
    space.gravity = (0, GRAVITY)

    # Create bucket instead of person
    bucket = Bucket(space)

    # Drops and slider setup
    drops = []
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

        # Bucket movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bucket.move("left")
        if keys[pygame.K_RIGHT]:
            bucket.move("right")

        # Drop generation
        rain_speed = slider.val
        frame_count += 1
        if frame_count >= (FPS // max(rain_speed, 1)):
            drop = create_drop(space)
            drops.append(drop)
            frame_count = 0

        # Step the physics simulation
        space.step(1 / FPS)

        # Shrink and remove drops that hit the bucket
        for drop in drops[:]:
            dx = abs(drop.body.position.x - bucket.body.position.x)
            dy = bucket.body.position.y - drop.body.position.y

            if dx < 35 and 0 < dy < 90:
                drop.custom_radius *= 0.9  # shrink the visual radius
                if drop.custom_radius < 1:
                    space.remove(drop, drop.body)
                    drops.remove(drop)

        # Draw everything
        draw_drops(screen, drops)
        bucket.draw(screen)
        slider.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()


