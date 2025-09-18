import area

shape = input("Enter shape which area need calculate (rectangle, triangle, circle): ").strip().lower()

if shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of rectangle:", area.area_of_rectangle(length, width))
elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle:", area.area_of_triangle(base, height))
elif shape == "circle":
    radius = float(input("Enter radius: "))
    print(f"Area of circle: {area.area_of_circle(radius):.3f}")