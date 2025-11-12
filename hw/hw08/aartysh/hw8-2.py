import re

password = input()
pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@])[A-Za-z\d$#@]{5,16}$'

if re.fullmatch(pattern, password):
    print("Password is valid")
else:
    print("Password is not valid")