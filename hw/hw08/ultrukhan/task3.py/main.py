import area_calculating as a

type = input("Choose the type of figure(rectangle, triangle, circle): ")

match type.lower():
    case "rectangle":
        a.area_of_rectangle()
    case "triangle":
        a.area_of_triangle()
    case "circle":
        a.area_of_circle()
    case _:
        print("Incorrect type of figure")

