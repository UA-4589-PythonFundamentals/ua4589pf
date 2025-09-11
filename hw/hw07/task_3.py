def char_count(word):
    result = {}
    for i in word:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

input_word = input("Enter a word: ")
print(char_count(input_word))


