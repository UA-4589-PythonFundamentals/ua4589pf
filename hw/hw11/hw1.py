class MyError (Exception):
    pass

def age_checker(raw_age):

    age = int(raw_age)

    if age < 0 :
        raise MyError(f'Your number "{age}" cannot be your age (must be 0 or greater).')
    elif age % 2 == 0:
        return f'Your age is even'
    else:
        return f'Your age is odd'

try:
    raw = input("Enter your age: ")

    print(age_checker(raw))

except MyError as e:
    print(e)
except ValueError:
    print(f'"{raw}" is not a valid age. Please enter a non-negative integer.')