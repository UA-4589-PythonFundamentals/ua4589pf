from math import pow, pi

def s_triangle():
    x = int(input('Write the length: '))
    y = int(input('Write the height: '))
    result = (x * y) / 2
    print(f'Area of triangle is {result}')
    return result


def s_circle():
        x = int(input('Write the radius:'))
        result = pi * pow(x, 2)
        print(f'Area of circle is {result}')
        return result

def s_rectangle():
    x = int(input('Write the length:'))
    y = int(input('Write the width:'))
    result = x * y
    print(f'Area of rectangle is {result}')
    return result


