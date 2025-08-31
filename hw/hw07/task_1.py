def max_of_two(a, b):
    """
    Функція повертає найбільше з двох чисал.
    """
    return a if a > b else b

if __name__ == "__main__":
    num1 = (input("Введите первое число: "))
    num2 = (input("Введите второе число: "))

    print("Большее число:", max_of_two(num1, num2))
