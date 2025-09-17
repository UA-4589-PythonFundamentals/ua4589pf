
#codewar
# I. Jenny's secret message
def jenny_greeting(name: str) -> str:
    return f'Hello, {name}' if name != 'Johnny' else f'I love you, {name}'
print(f'{jenny_greeting('Johnny') = }')
print(f'{jenny_greeting('Tom') = }')

# II. Find The Distance Between Two Points
def distance_points(a:tuple, b:tuple) -> float:
    return (a[1]-a[0])**2+(b[1]-b[0])**2
print(f'{distance_points((2,5), (5, 2))= }')

# III. No yelling!
def filter_words(text: str):
    return text.capitalize()
print(filter_words('HELLO CAN YOU HEAR ME'))
print(filter_words('now THIS is REALLY interesting'))

# IV. Convert a Number to a String
def convert_num_to_str(el: int)->str:
    return str(el)

print(convert_num_to_str(123), type(convert_num_to_str(123)))
print(convert_num_to_str(-100), type(convert_num_to_str(-100)))

# V. Reversing Words in a String
def reverse_str(el: str)->str:
    el = el.split()
    el = el[::-1]
    el = ' '.join(el)
    return el
print(reverse_str("Hello World"))
print(reverse_str("Hi There."))

# VI. Reverse List Order
def reverse_list(el: list)->list:
    return el[::-1]
print(reverse_list([1,2,3,4]))
print(reverse_list([9,2,0,7]))

# VII. Multiples of 3 or 5
def mupltiples_3_or_5(num):
    sum_num = 0
    for el in range(num):
        if el % 3 == 0 or el % 5 == 0:
            sum_num += el
    return sum_num
print(mupltiples_3_or_5(-5))

# VIII. Will you make it?
def will_you_make_it(speed, gallon):
    pump = 50
    return True if speed * gallon >= pump else False

# IX. Are You Playing Banjo?
def game_banjo(name: str) -> str:
    temp_name = name.lower()
    if temp_name.startswith('r'):
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'
print(game_banjo('Tom'))

# XI. Convert boolean values to strings 'Yes' or 'No'.
def convert_bool(a: bool) -> str:
    return 'Yes' if a else 'No'

# XI. Counting sheep
def count_sheeps(sheep):
    count = 0
    for el in sheep:
        if el == True:
            count += 1
    return count

#XII. Is this my tail?
def correct_tail(body, tail):
    return True if body[-1] == tail else False

def find_secret_message(paragraph):
    """Your job is to write a function that will find the secret words of the message and return them in order.
    The words in the secret message should be ordered in the order in which they are found as a duplicate, for example:
    'This is a test. this test is fun.' # --> 'this test is'"""
    for punctuation in ',.!?;-:':
        paragraph = paragraph.replace(punctuation, '')
    paragraph = paragraph.lower().split()

    seen = set()
    result = []
    for el in paragraph:
        if el in seen and el not in result:
            result.append(el)
        else:
            seen.add(el)
    result = ' '.join(result)
    return result