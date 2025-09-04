import math

def area_rectangle():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    area = a * b
    print("Area of rectangle =", area)
    return area

def area_triangle():
    b = float(input("Enter base of triangle: "))
    h = float(input("Enter height of triangle: "))
    area = 0.5 * b * h
    print("Area of triangle =", area)
    return area

def area_circle():
    r = float(input("Enter radius of circle: "))
    area = math.pi * pow(r, 2)
    print("Area of circle =", round(area, 2))
    return area
