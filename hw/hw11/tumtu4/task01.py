def odd_or_even(age):
    if age<0:
        raise ValueError("Age cannot be a negative number!")
    text = 'The age is '
    return text+'odd' if age%2 else text+'even'

if __name__=="__main__":
    try:
        user_age=int(input("Enter your age: "))
        print(odd_or_even(user_age))
    except ValueError as e:
        print(e)