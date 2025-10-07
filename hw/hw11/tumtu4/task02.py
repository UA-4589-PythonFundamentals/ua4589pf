class MyError(Exception):
    pass

def day_of_week(number):
    try:
        number=int(number)
        if not (0 < number < 8):
            raise MyError("Number outside the range!")
            
    except (ValueError, TypeError):
        raise MyError("Number must have only digits!")
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[number-1]

if __name__ == "__main__":
    try:
        number = input("Enter number between 1 to 7: ")
        print(day_of_week(number))
    except MyError as e:
        print(e)