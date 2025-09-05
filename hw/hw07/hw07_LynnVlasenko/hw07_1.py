# Task1. 
# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def get_largest_number(num1, num2):
  """
  Function with two positional arguments and returns the largest argument.
  """
  return max(num1, num2)

num1 = int(input("Enter a whole number:"))
num2 = int(input("Enter another whole number:"))

print(get_largest_number.__doc__)
print(get_largest_number(num1, num2))



# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

import math

geometric_figure = input("Enter the geometric figure name to get their area\n \
                         - ex: rectangle, triangle, circle): ")


def rectangle_area(length, width):
    """ Function to calculate the rectangle area """
    return length * width

def triangle_area(base, height):
    """ Function to calculate the triangle area """
    return 0.5 * base * height

def circle_area(radius):
    """ Function to calculate the circle area """
    return math.pi * radius * radius


match geometric_figure.lower():
    case "rectangle":
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))
        print(f"Rectangle Area = {rectangle_area(length, width)}")
    case "triangle":
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))
        print(f"Triangle Area = {triangle_area(base, height)}")
    case "circle":
        radius = float(input("Enter circle radius: "))
        print(f"Area of Circle = {circle_area(radius)}")
    case _:
        print("I can calculates the area of a rectangle, triangle or circle only")



# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}


# solution with Counter
from collections import Counter

input_text = input("Enter some text to calculates the number of each character into it:")

def count_char(text):
    """Function to calculates the number of each character in a string"""
    text_l = text.lower()
    filtered_text = "".join(ch for ch in text_l if ch.isalpha())
    return dict(Counter(filtered_text))

print(f"Result of character calculation is {count_char(input_text)}")


# solution with loop

# def count_char(text):
#     """Function to calculates the number of each character in a string"""
#     result = {}
#     text_l = text.lower()
#     filtered_text = "".join(ch for ch in text_l if ch.isalpha())
#     for char in filtered_text:
#         if char in result:
#             result[char] += 1
#         else:
#             result[char] = 1
#     return result

# print(f"Result of character calculation is {count_char(input_text)}")


# solution with comprehension

# def count_char(text):
#     text_l = text.lower()
#     filtered_text = "".join(ch for ch in text_l if ch.isalpha())
#     return {char: filtered_text.count(char) for char in set(filtered_text)}

# print(f"Result of character calculation is {count_char(input_text)}")