#task 1
def largest_num(a, b):
    """Return the largest number of two numbers"""

    return a if a > b else b

print(largest_num.__doc__)
print(largest_num(float(input("Enter the first number: ")), float(input("Enter the second number: "))))

#task 2
import numpy as np

def area_of_rectangle(a, b):
    """Calculates the area of a rectangle"""
    return a * b

def area_of_triangle(a, h):
    """Calculates the area of a triangle"""
    return 0.5 * a * h

def area_of_circle(r):
    """Calculates the area of a circle"""
    return np.pi * r ** 2

type = input("Choose the type of figure(rectangle, triangle, circle): ")

match type.lower():
    case "rectangle":
        print(area_of_rectangle(float(input("Enter a: ")), float(input("Enter b: "))))
    case "triangle":
        print(area_of_triangle(float(input("Enter a: ")), float(input("Enter h: "))))
    case "circle":
        print(area_of_circle(float(input("Enter radius: "))))
    case _:
        print("Incorrect type of figure")

#task 3
def num_of_char(str):
    """Calculates the number of characters included in given string"""
    res = {}
    for i in str:
        res.setdefault(i, str.count(i))
    return res

print(f"Result: {num_of_char(list(input("Your string is: ")))}")