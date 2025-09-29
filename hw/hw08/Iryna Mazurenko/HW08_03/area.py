import math

def rectangle_area(a, b):

    if a <= 0 or b <= 0:
        raise ValueError("Both sides of the rectangle must be positive numbers.")
    return a * b

def triangle_area(base, height):

    if base <= 0 or height <= 0:
        raise ValueError("Base and height of the triangle must be positive numbers.")
    return 0.5 * base * height

def circle_area(r):

    if r <= 0:
        raise ValueError("Radius of the circle must be a positive number.")
    return math.pi * pow(r, 2)
