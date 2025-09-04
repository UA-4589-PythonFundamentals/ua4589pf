import area
print(dir(area))
print(area.__file__)

def main():
    choose = int(input("Rectangle - 1\nTriangle - 2\nCircle - 3\nYour choice: "))
    if choose == 1:
        area.area_rectangle()
    elif choose == 2:
        area.area_triangle()
    elif choose == 3:
        area.area_circle()
    else:
        print("Wrong input")

if __name__ == "__main__":
    main()
