class MyError(Exception):
    def __init__(self, day):
        self.day = day
    def __str__(self):
        return f"Invalid type number: {self.day}. Please enter a number between 1 and 7."



def day_of_week(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        day = int(day)
        if day < 1 or day > 7:
            raise MyError(day)
        return days[day]
    except ValueError:
        return "Invalid input. Please enter a valid number between 1 and 7."
    except MyError as e:
        return e

user_input = input("Enter a number between 1 and 7: ")
print(day_of_week(user_input))