# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.


def process_age(age: int) -> str:
    if age < 0:
        raise ValueError("Age cannot be a negative! -> Enter a positive integer, please.")
    if age % 2 == 0:
        return f"You are {age} years old! The age is EVEN."
    else:
        return f"You are {age} years old! The age is ODD."

while True:
    try:
        user_age = int(input("Enter your age in numbers: ").strip())
        processed_age = process_age(user_age)
        print(processed_age)
        break
    except ValueError as e:
        print(f"Input error: The program expects a number! -> {type(e).__name__}: {e} \n Try again!\n")