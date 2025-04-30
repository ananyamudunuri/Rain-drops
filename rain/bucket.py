# rain/bucket.py

import pymunk
from config import WIDTH

class Bucket:
    def __init__(self, space):
        self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.body.position = (WIDTH // 2, 520)

        # Dimensions
        w = 100  # width
        h = 40   # height

        # U-shaped bucket: left wall, right wall, bottom
        self.shapes = [
            pymunk.Segment(self.body, (-w // 2, 0), (-w // 2, -h), 5),
            pymunk.Segment(self.body, (w // 2, 0), (w // 2, -h), 5),
            pymunk.Segment(self.body, (-w // 2, -h), (w // 2, -h), 5)
        ]

        for shape in self.shapes:
            shape.elasticity = 0.8

        # Add body and all shapes at once
        space.add(self.body, *self.shapes)

    def move(self, direction):
        speed = 300  # pixels/sec
        x, y = self.body.position
        if direction == "left":
            x = max(60, x - speed / 60)
        elif direction == "right":
            x = min(WIDTH - 60, x + speed / 60)
        self.body.position = (x, y)

    def get_shapes(self):
        return self.shapes

