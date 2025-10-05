from math import pi, pow

logo = r"""
  ____      _            _       _             
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | (__| |_| | | (_| | || (_) | |   
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
 """

def area_of_rectangle():
    """Calculates the area of rectangle"""
    side1 = None
    side2 = None
    while True:
        side1 = float(input("Enter the length of first side of rectangle: "))
        side2 = float(input("Enter the lenght of second side of rectangle: "))
        if side1 >0 and side2 > 0:
            break
        else:
            print("Sides can't be less than 0!")
    result = side1*side2
    print(f"Area of rectangle equals {result}")

def area_of_triangle():
    """Calculates the area of triangle"""
    base = None
    height = None
    while True:
        base = float(input("Enter base side of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        if base > 0 and height > 0:
            break
        else:
            print("Base and height can't be less than 0!")
    result = base*height*0.5
    print(f"Area of triangle equals {result}")
    
def area_of_circle():
    """Calculates the are of circle"""
    radius = None
    while True:
        radius = float(input("Enter the radius of circle: "))
        if radius > 0:
            break
        else:
            print("Radius can't be less or equal 0!")
    result = round(pi*pow(radius,2),2)
    print(f"Area of circle equals {result}")

if __name__ == "__main__":
    print(logo)