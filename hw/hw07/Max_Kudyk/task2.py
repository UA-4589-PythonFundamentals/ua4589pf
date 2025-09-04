def area_rectangle():
    a = int(input("Enter side a\n"))
    b = int(input("Enter side b\n"))
    print("Area of rectangle =", a*b)

def area_triangle():
    b = int(input("Enter base of triangle\n"))
    h = int(input("Enter height of triangle\n"))
    print("Area of triangle =", 0.5*b*h)

def area_circle():
    r = int(input("Enter radius of circle\n"))
    PI=3.14
    print("Area of circle =", PI*r**2)

def main():
    choose=int(input("Rectangle-1\nTriangle-2\nCircle-3\n"))
    if choose == 1:
        area_rectangle()
    elif choose == 2:
        area_triangle()
    elif choose == 3:
        area_circle()
    else:
        print("Wrong input")
    
main()