
# Task 1: Find the largest of two numbers using a function.

def largest_number(a, b):
    return a if a > b else b

print(largest_number(60, 565))


# Task 2: Calculate the area of different shapes using functions.

import math

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

# Main program
def main():
    print("Choose a shape: rectangle, triangle, circle")
    choice = input("Enter your choice: ").lower()

    if choice == "rectangle":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of rectangle:", rectangle_area(l, w))

    elif choice == "triangle":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of triangle:", triangle_area(b, h))

    elif choice == "circle":
        r = float(input("Enter radius: "))
        print("Area of circle:", circle_area(r))

    else:
        print("Invalid choice")

# Run program
main()



# Task 3: Count the occurrences of each character in a string using a function.

def count_characters(s):

    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

print(count_characters("hello"))
