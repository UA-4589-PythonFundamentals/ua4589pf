
def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return 3.14 * radius ** 2

shape = input("Choose area of shape (rectangle, triangle, circle): ")

if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(area_rectangle(length, width))
elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print(area_triangle(base, height))
elif shape == "circle":
    radius = float(input("Enter radius: "))
    print(area_circle(radius))

