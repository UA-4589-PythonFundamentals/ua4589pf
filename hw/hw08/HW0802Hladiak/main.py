from math import pi, pow
import areas

print("Choose a figure to calculate the area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter your choise (1,2,3): ")

if choice == "1":
    a = float(input("Enter the length (a): "))
    b = float(input("Enter the width (b): "))
    result = areas.rectangle_area(a, b)
    print(f"The area of the rectangle is: {result}")

elif choice == "2":
    a = float(input("Enter the base (a): "))
    h = float(input("Enter the height (h): "))
    result = areas.triangle_area(a, h)
    print(f"The area of the triangle is: {result}")

elif choice == "3":
    r = float(input("Enter the radius (r): "))
    result = areas.circle_area(r)
    print(f"The area of the circle is: {result}")

else:
    print("Invalid choice!")
