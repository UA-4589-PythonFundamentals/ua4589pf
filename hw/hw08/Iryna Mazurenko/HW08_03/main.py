import area

print("Choose a figure to calculate area:")
print("\033[92m1. Rectangle\033[0m")
print("\033[91m2. Triangle\033[0m")
print("\033[94m3. Circle\033[0m")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    print("\033[92mRectangle area:", area.rectangle_area(a, b), "\033[0m")

elif choice == "2":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("\033[91mTriangle area:", area.triangle_area(base, height), "\033[0m")

elif choice == "3":
    r = float(input("Enter radius: "))
    print("\033[94mCircle area:", area.circle_area(r), "\033[0m")

else:
    print("Invalid choice!")
