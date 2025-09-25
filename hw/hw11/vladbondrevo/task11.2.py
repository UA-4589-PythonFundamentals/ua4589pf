class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

        
def day():
    try:
        num = int(input("Enter number which corresponds with day of the week: "))
        if num > 7:
            raise MyError("Incorrect number of days in week")
        elif num == 1:
            print("First day is Monday")
        elif num == 2:
            print("Second day is Tuesday")
        elif num == 3:
            print("Third day is Wednesday")
        elif num == 4:
            print("Fourth day is Thursday")
        elif num == 5:
            print("Fifth day is Friday")
        elif num == 6:
            print("Sixth day is Saturday")
        elif num == 7:
            print("Last day is Sunday")
    except MyError as m:
        print(f"Error: {m.msg}")
    except ValueError:
        print("Entered non-numerical data")
        
day()  

