#task num. 2

answer = input('The program calculate area of triangle, rectangle and circle writhe what you want calculate:')

PI = 3.14159

if answer.lower() == 'triangle':
    def s_triangle():
        x = int(input('Write the length: '))
        y = int(input('Write the height: '))
        result = (x * y) / 2
        return result
    print(f'Area of triangle is {s_triangle()}')

elif answer.lower() == 'rectangle':
    def s_rectangle():
        x = int(input('Write the length:'))
        y = int(input('Write the width:'))
        result = x * y
        return result
    print(f'Area of rectangle is {s_rectangle()}')

elif answer.lower() == 'circle':
    def s_circle():
        x = int(input('Write the radius:'))
        result = PI * x ** 2
        return result
    print(f'Area of circle is {s_circle()}')

else:
    print('Your type of input is wrong, try again')

