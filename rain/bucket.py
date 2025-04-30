# rain/bucket.py
import pymunk

def create_bucket(space):
    bucket = pymunk.Segment(space.static_body, (300, 500), (500, 500), 10)
    bucket.elasticity = 0.8
    space.add(bucket)
    return bucket
