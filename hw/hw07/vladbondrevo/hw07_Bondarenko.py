num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

def largest(num1, num2):
    """This function finds the largest number between two numbers"""
    if num1 > num2:
        return num1
    else:
        return num2

print(largest(num1, num2))


def rect(length, width):
    """This function calculates area of a rectangle"""
    return length * width

def tri(base, height):
    """This function calculates area of a triangle"""
    return base * height/2

def circ(radius, pi = 3.14):
    """This function calculates area of a circle"""
    return pi * radius ** 2

choise = input("Enter the figure number: ")

if choise == "1":
    length = float(input("Enter length:"))
    width = float(input("Enter width:"))
    print("Area of rectangle:", rect(length, width))

elif choise == "2":
    base = float(input("Enter base:"))
    height = float(input("Enter height:"))
    print("Area of triangle:", tri(base, height))

elif choise == "3":
    radius = float(input("Enter radius:"))
    print("Area of circle:", circ(radius))

else:
    print("Wrong choise")

word = str(input("Enter word:"))


def calc(word, out = {}):
    """This function calculates the number of characters included in given string"""
    for i in word:
        out[i] = out.setdefault(i, 0) + 1
    return out

print(calc(word))
