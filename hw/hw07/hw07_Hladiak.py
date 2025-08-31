import math


def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return math.pi * radius ** 2


choise = input("Введіть номер фігури: 1, 2, 3 -->")


if choise == "1":
    length = float(input("введіть довжину:"))
    width = float(input("введіть ширину:"))
    print("Площа прямокутника:", rectangle_area(length, width))

elif choise == "2":
    base = float(input("введіть основу:"))
    height = float(input("введіть висоту:"))
    print("Площа трикутника:", triangle_area(base, height))

elif choise == "3":
    radius = float(input("введіть параметр:"))
    print("Площа кола:", circle_area(radius))

else:
    print("Wrong choise")


def char_count(string):
    counts = {}
    for ch in string:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


word = input("введіть слово:")
print(char_count(word))


def max_of_two(a, b):
    return a if a > b else b


print(max_of_two(40, 23))
