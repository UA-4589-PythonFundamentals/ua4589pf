import hw08
choise = input("Enter the figure number: ")

if choise == "1":
    length = float(input("Enter length:"))
    width = float(input("Enter width:"))
    print("Area of rectangle:", hw08.rect(length, width))

elif choise == "2":
    base = float(input("Enter base:"))
    height = float(input("Enter height:"))
    print("Area of triangle:", hw08.tri(base, height))

elif choise == "3":
    radius = float(input("Enter radius:"))
    print("Area of circle:", hw08.circ(radius))

else:
    print("Invalid choise")
