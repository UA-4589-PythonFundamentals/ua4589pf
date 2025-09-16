import re

def check(pat, pas):
    if not re.search(pat, pas):
        print(f"Your password have to contain at least 1 character between {pat}, try again.")
        return False
    return True

password = input("Input your password(it has to contain at least 1 character from a-z, A-Z, 0-9, @#$ and to be 6-16 characters in length): ")

if 6 <= len(password) <= 16:
    correct = True
    correct = check("[a-z]", password)
    correct = check("[A-Z]", password)
    correct = check("[0-9]", password)
    correct = check("[@#$]", password)
    if correct == True:
        print("Your password is perfect!")
else:
    print("Your password between 6 and 16 characters, try again")
