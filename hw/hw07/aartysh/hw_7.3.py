#Task 1
def greet(name: str):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

#Task 2
def distance(x1, y1, x2, y2: float):
    result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(result, 2)

#Task 3
def filter_words(st: str):
    return " ".join(st.split()).capitalize()

#Task 4
def number_to_string(num: int):
    return str(num)

#Task 5
def reverse(st: str):
    return " ".join(reversed(st.split()))

#Task 6
def reverse_list(l: list):
    l.reverse()
    return l

#Task 7
def solution(number: int):
    if number <= 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#Task 8
def zero_fuel(distance_to_pump, mpg, fuel_left: int):
    return mpg * fuel_left >= distance_to_pump

#Task 9
def are_you_playing_banjo(name: str):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
#Task 10
def bool_to_word(boolean: bool):
    return "Yes" if boolean else "No"

#Task 11
def count_sheeps(sheep: list):
    result = 0
    for animal in sheep:
        if animal == True:
            result += 1
    return result

#Task 12
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False