class AgeError(Exception):
    def __init__(self, message = "You can't exist. Enter valid number"):
        self.data = message

def check_age(age):
    if age <= 0:
        raise AgeError()
    return "Your age is Even" if age % 2 == 0 else "Your age is Odd"

try:
    age = int(input("Enter you age: "))
    odd_or_even = check_age(age)
    print(odd_or_even)
except ValueError:
    print("That's not a number!")
except AgeError as e:
    print(e.data)
    



