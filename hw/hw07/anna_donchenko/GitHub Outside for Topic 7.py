# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"



# II. Find The Distance Between Two Points
def distance(a, b):
    return round(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5, 2)



# III. No yelling!
def format_text(text):
    # Remove extra spaces and split into words
    words = text.split()
    
    # Lowercase all words
    words = [word.lower() for word in words]
    
    # Capitalize the first word only
    if words:
        words[0] = words[0].capitalize()
    
    # Join back into a sentence
    return ' '.join(words)



# IV. Convert a Number to a String
def int_to_str(n):
    return str(n)
# or
def int_to_str(n):
    return f"{n}"


# V. Reversing Words in a String
def reverse_words(s):
    words = s.strip().split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


# VI. Reverse List Order
def reverse_list(lst):
    return lst[::-1]



# VII. Multiples of 3 or 5
def solution(number):
    if number <= 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)



# VIII. Will you make it?
def can_reach_pump(distance_to_pump, mpg, gallons_left):
    return gallons_left * mpg >= distance_to_pump



# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"



# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(value):
    return "Yes" if value else "No"



# XI. Counting sheep
def count_sheeps(sheep_list):
    return sheep_list.count(True)



# XII. Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail


    


