import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
   return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

print("Select a geometric figure to calculate the area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = input("Your choice (1/2/3): ")

if choice == "1":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = area_rectangle(length, width)
    print(f"Area of the rectangle: {area}")

elif choice == "2":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = area_triangle(base, height)
    print(f"Area of the triangle: {area}")

elif choice == "3":
    radius = float(input("Enter the radius of the circle: "))
    area = area_circle(radius)
    print(f"Area of the circle: {area}")

else:
    print("Invalid choice. Please select 1, 2, or 3.")