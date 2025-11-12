import math

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
    area = math.pi * radius ** 2
    return area

print("Choose a shape to calculate the area.\n\n1. Triangle\n2. Rectangle\n3. Circle\n")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    triangle_base = int(input("Enter base size of triangle: "))
    triangle_height = int(input("Enter height size of triangle: "))
    print(f"Triangle area is — {triangle_area(triangle_base, triangle_height)}")

elif choice == "2":
    rectangle_length = int(input("Enter length size of rectangle: "))
    rectangle_width = int(input("Enter width size of rectangle: "))
    print(f"Rectangle area is — {rectangle_area(rectangle_length, rectangle_width)}")

elif choice == "3":
    circle_radius = int(input("Enter radius size of circle: "))
    print(f"Circle area is — {round(circle_area(circle_radius), 2)}")

else:
    print("Entered wrong number.")