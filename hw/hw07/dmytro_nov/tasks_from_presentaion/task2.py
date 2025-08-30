from math import pi

#TASK2

def area_of_rectangle():
    """Calculates the area of rectangle"""
    while True:
        side1 = float(input("Enter the length of first side of rectangle: "))
        side2 = float(input("Enter the lenght of second side of rectangle: "))
        if side1 > 0 and side2 > 0:
            break
        else:
            print("Sides of rectangle must be greater than 0!")
    result = side1*side2
    print(f"Area of rectangle equals {result}")

def area_of_triangle():
    """Calculates the area of triangle"""
    while True:
        base = float(input("Enter base side of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        if base > 0 and height > 0:
            break
        else:
            print("Base and height must be greater than 0!")
    result = base*height*0.5
    print(f"Area of triangle equals {result}")
    
def area_of_circle():
    """Calculates the are of circle"""
    while True:
        radius = float(input("Enter the radius of circle: "))
        if radius > 0:
            break
        else:
            print("Invalid input\nRadius must be greater than 0")
    result = pi*radius**2
    print(f"Area of circle equals {result}")


while True:
    user_choice = input("What shape do you need to find the area of: rectangle, triangle or circle? (r,t,c): ").lower()
    if user_choice == "r":
        area_of_rectangle()
        break
    elif user_choice == "t":
        area_of_triangle()
        break
    elif user_choice == "c":
        area_of_circle()
        break
    else:
        print("Invalid choice\nTry once more")
