def get_day_of_week(number):
    """Return the name of the weekday for a given number (1–7)."""
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if number not in days:
        raise ValueError("Number must be between 1 and 7.")
    return days[number]


def main():
    try:
        user_input = input("Enter a number (1–7): ")
        number = int(user_input)
        day = get_day_of_week(number)
        print(f"The day of the week is: {day}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
