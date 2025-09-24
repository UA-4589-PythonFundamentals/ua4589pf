num = input("Enter a number: ")


def check_odd_even(num):
    try:
        num = int(num)
        if num < 0:
            return "You entered a negative number."
        elif num % 2 == 0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except ValueError:
        return "Invalid input! Please enter a valid integer."


print(check_odd_even(num))
