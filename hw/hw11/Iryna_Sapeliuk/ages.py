
class MyError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"You input negative age: {self.age}."

def check_age(age):
   if age > 0:
       if age % 2 == 0:
           return("Even age")
       else:
           return("Odd age")
   else:
       return(MyError(age))
   
ages = (int(input("Enter age: ")))
print(check_age(ages))