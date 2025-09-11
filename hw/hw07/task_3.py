def number_of_characters(word):
    num_of_char = dict()
    for i in word:
        num_of_char[i] = num_of_char.get(i, 0) + 1
    return num_of_char

word = input("Enter a word: ")
print(number_of_characters(word))