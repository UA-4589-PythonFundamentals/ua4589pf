import areas                

def main():
    figure = input("Which figure's area do you want to calculate? (rectangle/triangle/circle): ").strip().lower()

    if figure == "rectangle":
        a = int(input("Enter length a: "))
        b = int(input("Enter width b: "))
        area = areas.rectangle_area(a, b)
        print(f"Rectangle area: {area}")

    elif figure == "triangle":
        h = int(input("Enter height h: "))
        a = int(input("Enter base a: "))
        area = areas.triangle_area(h, a)
        print(f"Triangle area: {area}")

    elif figure == "circle":
        r = int(input("Enter radius r: "))
        area = areas.circle_area(r)
        print(f"Circle area: {area}")

    else:
        print("Unknown figure")

if __name__ == "__main__":
    main()