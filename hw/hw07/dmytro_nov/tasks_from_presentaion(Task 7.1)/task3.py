#TASK 3 

#First option
def characters(word):
    num_of_char = dict()
    for char in word:
        num_of_char[char] = num_of_char.get(char,0) + 1
    return num_of_char

#second option
# def characters(word):
#     num_of_char = {}
#     for char in word:
#         if char not in num_of_char:
#             num_of_char[char] = 1
#         else:
#             num_of_char[char] +=1
#     return num_of_char

# print(characters("hello"))
# print(characters("bigger words it is"))