def num_of_char(word: str):
    """
    Calculate the number of character in a string.
    """
    result = {}
    for letter in word:
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result