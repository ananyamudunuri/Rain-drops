# rain/drop.py

import random
import pymunk
from config import DROP_RADIUS

def create_drop(space):
    mass = 1
    radius = DROP_RADIUS
    x = random.randint(100, 700)  # Random x-position near the top
    y = 0                         # Spawn at top of screen

    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = (x, y)
    shape = pymunk.Circle(body, radius)
    shape.custom_radius = radius  # manually track radius

    shape.elasticity = 0.6

    space.add(body, shape)
    return shape
