import math

def area_of_rectangle():
    """Calculates the area of a rectangle"""
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print(f"The area of a rectangle is {a * b}")
    return a * b

def area_of_triangle():
    """Calculates the area of a triangle"""
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    print(f"The area of a triangle is {0.5 * a * h}")
    return 0.5 * a * h

def area_of_circle():
    """Calculates the area of a circle"""
    r = float(input("Enter radius: "))
    print(f"The area of a circle is {math.pi * math.pow(r, 2)}")
    return math.pi * math.pow(r, 2)