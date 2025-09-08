import re

password = input("Enter your password = ")


if len(password) < 6 or len(password) > 16:
    print("Invalid password: incorrect length")

elif (re.search("[a-z]", password) and
      re.search("[A-Z]", password) and
      re.search("[0-9]", password) and
      re.search("[$#@]", password)):
    print("Password is valid")
else:
    print("Invalid password")
