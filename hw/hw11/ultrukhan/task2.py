class DayNum(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.message = msg

week = {
    1:"Monday",
    2:"Tuesday",
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"
}

day = int(input("Enter the number of the day: "))
try:
    if day in week:
        print(week[day])
    else:
        raise DayNum("entered number must be from 1 to 7")
except ValueError:
    print(ValueError("You should enter the int number from 1 to 7"))
except DayNum as dn:
    print(f"Your exception is: {dn}")