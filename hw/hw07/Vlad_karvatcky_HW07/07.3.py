def calculate_charachters():
    string = input("Input something: ")
    count = {}
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    print(count)
calculate_charachters()