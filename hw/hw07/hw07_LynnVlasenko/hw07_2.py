# Tasks from codewars 
# (link to my account: https://www.codewars.com/users/LynnVlasenko/completed_solutions)

# I. Jenny's secret message___________________________________________________________
# DESCRIPTION:
# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him slightly different. 
# She added a special case to her function, but she made a mistake.
# Can you help her?

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


# II. Find The Distance Between Two Points____________________________________________
# DESCRIPTION:
# Given two ordered pairs calculate the distance between them. Round to two decimal places. 
# This should be easy to do in 0(1) timing.

def distance(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return round(d, 2)

# II_2 Solution with math
# import math

# def distance(x1, y1, x2, y2):
#     d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#     return round(d, 2)


# III. No yelling!____________________________________________________________________
# DESCRIPTION:
# Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. 
# String should be capitalized and properly spaced. Using re and string is not allowed.

# Examples:
# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
# filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
# filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!

def filter_words(st):
    words = st.split()
    sentence = " ".join(words).lower()
    return sentence.capitalize()


# IV. Convert a Number to a String_____________________________________________________
# DESCRIPTION:
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    return str(num)


# V. Reversing Words in a String_______________________________________________________
# DESCRIPTION:
# You need to write a function that reverses the words in a given string. 
# Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# Example (Input --> Output)
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"

def reverse(st):
    st_list = st.strip().split(" ")
    st = " ".join(st_list[::-1])
    return st


# VI. Reverse List Order_______________________________________________________________
# DESCRIPTION:
# In this kata you will create a function that takes in a list and returns a list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
    return l[::-1]


# VII. Multiples of 3 or 5_____________________________________________________________
# DESCRIPTION:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If a number is a multiple of both 3 and 5, only count it once.

def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)


# VIII. Will you make it?_______________________________________________________________
# DESCRIPTION:
# You were camping with your friends far away from home, but when it's time to go back, 
# you realize that your fuel is running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


# IX. Are You Playing Banjo?___________________________________________________________
# DESCRIPTION:
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        name += " plays banjo"
    else:
        name += " does not play banjo"
    return name


# X. Convert boolean values to strings 'Yes' or 'No’___________________________________
# DESCRIPTION:
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# XI. Counting sheep___________________________________________________________________
# DESCRIPTION:
# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    return sum(1 for s in sheep if s is True)

# XI_2 solution with count:
# def count_sheeps(sheep):
#     return sheep.count(True)


# XII. Is this my tail?_______________________________________________________________
# DESCRIPTION:
# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. 
# To help her, you must correct the broken function to make sure that the second argument (tail), 
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.

# The arguments will always be non empty strings, and normal letters.

# Function with errors given in the task:

# def correct_tail(body, tail):
#      sub = body.substr(len(body)-len(tail.length)
#         if sub = tai:
#     return True
#         else:
#     return False
        
#     Fixing an existing function:

# def correct_tail(body, tail):
#     sub = body[len(body) - len(tail):]
#     if sub == tail:
#         return True
#     else:
#         return False


#     My solutions:
# def correct_tail(body, tail):
#     return body[-1] == tail

def correct_tail(body, tail):
    return body.endswith(tail)