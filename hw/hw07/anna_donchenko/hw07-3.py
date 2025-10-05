def char_count(word):
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1
    return counts
result = char_count("hello")
print(result)