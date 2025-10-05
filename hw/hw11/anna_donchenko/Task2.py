def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number in days:
        return f"The day is {days[number]}."
    else:
        return "Invalid number. Please enter a number between 1 and 7."

def main():
    try:
        user_input = input("Enter a number (1-7) to get the corresponding day of the week: ")
        number = int(user_input)
        result = get_day_of_week(number)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
