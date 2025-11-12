from math import pi, pow

def triangle_area(base: int, height: int):
    """
    Returns the area of triangle.
    """
    area = base * height * 0.5
    return area

def rectangle_area(length: int, width: int):
    """
    Returns the area of rectangle.
    """
    area = length * width
    return area

def circle_area(radius: int):
    """
    Returns the area of circle.
    """
    area = pi * radius ** 2
    return area