def char_count(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result


if __name__ == "__main__":
    text = input("Введіть рядок: ")
    print(char_count(text))
