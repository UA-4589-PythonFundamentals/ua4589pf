days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

try:
    day_number = int(input("Enter the number of the day of the week (1-7): "))

    day_name = days_of_week.get(day_number)

    if day_name:
        print(f"✅ Day {day_number} of the week is {day_name}.")
    else:
        print("Error: No such day of the week exists. Please enter a number from 1 to 7")

except ValueError:
    print("Error: Non-numeric data entered. Please enter a number")