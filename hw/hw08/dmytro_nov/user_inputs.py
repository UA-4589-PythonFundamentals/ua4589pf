from area import area_of_circle,area_of_rectangle,area_of_triangle, logo

print(logo)
print("\n\n Welcome to area calculator")

while True:
    user_choice = input("What shape do you need to find the area of: rectangle, triangle or circle? (r,t,c)").lower()
    if user_choice == "r" or user_choice == "rectangle":
        area_of_rectangle()
    elif user_choice == "t" or user_choice == "triangle":
        area_of_triangle()
    elif user_choice == "c" or user_choice == "circle":
        area_of_circle()
    else:
        print("Invalid choice\nTry once more")
        continue

    cont = input("One more shape? (y/n)").lower()
    if cont == "n":
        print("Have a nice day!")
        break
