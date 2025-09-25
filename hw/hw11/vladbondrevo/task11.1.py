class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

        
def define():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise MyError("Entered negative number")
        if age % 2 == 0:
            print("Your age is even")
        else:
            print("Your age is odd")
    except MyError as m:
        print(f"Error: {m.msg}")
        
define()    


