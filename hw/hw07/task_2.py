import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2


if __name__ == "__main__":
    print("Що ви хочете обчислити?")
    print("1 - Площа прямокутника")
    print("2 - Площа трикутника")
    print("3 - Площа кола")

    choice = input("Введіть номер вибору: ")

    if choice == "1":
        l = float(input("Введіть довжину: "))
        w = float(input("Введіть ширину: "))
        print("Площа прямокутника:", area_rectangle(l, w))

    elif choice == "2":
        b = float(input("Введіть основу: "))
        h = float(input("Введіть висоту: "))
        print("Площа трикутника:", area_triangle(b, h))

    elif choice == "3":
        r = float(input("Введіть радіус: "))
        print("Площа кола:", area_circle(r))

    else:
        print("Некоректний вибір!")
