# Write a program that analyzes the entered number and, depending on the number, gives
# the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.). Take
# into account cases of entering numbers from 8 and more, as well as cases of entering non-
# numerical data.

def weekday_generator(num: int) -> str:
    if num < 1 or num > 7:
        raise ValueError("There are only seven days in a week. -> Enter a number from 1 to 7, please.")

    weekdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekdays_list[num - 1]

while True:
    weekday_num_input = input("Enter the day of the week number: ")
    try:
        weekday_num = int(weekday_num_input)
        weekday_name = weekday_generator(weekday_num)
        print(f"Day {weekday_num} is {weekday_name}")
        break
    except ValueError as e:
        print(f"Input error: The program expects a number! -> {type(e).__name__}: {e} \n Try again!\n")