from math import pi, pow

def rectangle_area(length, width):
    """ Function to calculate the rectangle area """
    return length * width

def triangle_area(base, height):
    """ Function to calculate the triangle area """
    return 0.5 * base * height

def circle_area(radius):
    """ Function to calculate the circle area """
    return round(pi * pow(radius, 2), 2)