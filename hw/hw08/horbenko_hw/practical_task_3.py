import math

def rectangle(a, b):
    return f'S = {a * b}'

def triangle(h, a):
    return f'S = {0.5 * h * a}'

def circle(r):
    return f'S = {math.pi * math.pow(r, 2)}'

def area_calculator():
    figure = input("Enter figure (rectangle/triangle/circle): ").lower()

    if figure == 'rectangle':
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        print(rectangle(a, b))

    elif figure == 'triangle':
        h = int(input("Enter height: "))
        a = int(input("Enter base: "))
        print(triangle(h, a))

    elif figure == 'circle':
        r = int(input("Enter radius: "))
        print(circle(r))

    else:
        print('Wrong figure')