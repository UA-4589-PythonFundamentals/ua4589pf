class MyError(Exception):
    def __init__(self, message):
        self.data = message

week = {"1":"Monday",
        "2":"Tuesday",
        "3":"Wednesday",
        "4":"Thursday",
        "5":"Friday",
        "6":"Saturday",
        "7":"Sunday"
        }


user_input = input("Enter your number(>0):" )
# if user_input.isdigit():
#     number = str(int(user_input)%7)
#     print(f"{user_input} correspons to {week[number]}")
try:
    user_input = int(user_input)
    if user_input <= 0:
        raise MyError("Input must be greater than 0")
except ValueError:
    print("Your input is invalid. It should've been number")
except MyError as e:
    print(e.data)
else:
    number = str(user_input % 7)
    print(f"Your input {user_input} corresponds to {number} and that means that you've chosen {week[number]}")

