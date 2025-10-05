#Task 1: Jenny's secret message

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return f"Hello, {name}!"

#Task 2: Find The Distance Between Two Points

# def distance(x1, y1, x2, y2):
#     return round(((x2-x1)**2+(y2-y1)**2)**0.5,2)

#Task 3: No yelling!

# def filter_words(st):
    # return " ".join(st.capitalize().split())

#Task 4: Convert a Number to a String!

# def number_to_string(num):
    # return str(num)

#Task 5: Reversing Words in a String

# def reverse(st):
#     # Your Code Here
#     l1 = st.split()
#     result = ""
#     for k, v in enumerate(l1[::-1]):
#         l1[k] = v
#     return " ".join(l1)

#Task 6: Reverse List Order

# def reverse_list(l):
#     return l[::-1]

#Task 7: Multiples of 3 or 5

# def solution(number):
#     sum = 0 
#     for n in range(number):
#         if n % 3 == 0 or n % 5 == 0:
#             sum+=n
            
#     return sum
  
#Task 8: Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump <= mpg*fuel_left

#Task 9: Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     # Implement me!
#     if name.lower()[0] == "r":
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

#Task 10: Convert boolean values to strings 'Yes' or 'No'.

# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"

#Task 11: Counting sheep...

# def count_sheeps(sheep):
#     count = 0
#     for s in sheep:
#         if s:
#             count += 1
#     return count

#Task 12: Is this my tail?

# def correct_tail(body, tail):
#     return tail == body[-1]