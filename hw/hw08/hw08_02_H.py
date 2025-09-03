import re

password = input("input password = ")


if len(password) < 6 or len(password) > 16:
    print("Invalid password")

elif (re.search(r"[a-z]", password) and
      re.search(r"[A-Z]", password) and
      re.search(r"[0-9]", password) and
      re.search(r"[$#@]", password)):
    print("Password is valid")
else:
    print("Invalid password: missing required characters")