import hm08task3def

answer = input('The program calculate area of triangle, rectangle and circle writhe what you want calculate:')

if answer.lower() == 'triangle':
    hm08task3def.s_triangle()

elif answer.lower() == 'rectangle':
    hm08task3def.s_rectangle()

elif answer.lower() == 'circle':
    hm08task3def.s_circle()

else:
    print('Your type of input is wrong, try again')