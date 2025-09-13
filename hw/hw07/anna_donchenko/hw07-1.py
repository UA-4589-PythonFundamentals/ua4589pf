def max_of_two(a, b):
    """
    Returns the largest of two numbers.
    """
    return a if a > b else b
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

result = max_of_two(a, b)
print("Більше число:", result)

