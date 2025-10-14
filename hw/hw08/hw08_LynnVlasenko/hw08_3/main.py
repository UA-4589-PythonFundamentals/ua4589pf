import area_calculator as ar

geometric_figure = input("Enter the geometric figure name to get their area\n \
                         - ex: rectangle, triangle, circle): ").strip().lower()

match geometric_figure:
    case "rectangle":
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))
        print(f"Rectangle Area = {ar.rectangle_area(length, width)}")
    case "triangle":
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))
        print(f"Triangle Area = {ar.triangle_area(base, height)}")
    case "circle":
        radius = float(input("Enter circle radius: "))
        print(f"Area of Circle = {ar.circle_area(radius)}")
    case _:
        print("I can calculates the area of a rectangle, triangle or circle only")