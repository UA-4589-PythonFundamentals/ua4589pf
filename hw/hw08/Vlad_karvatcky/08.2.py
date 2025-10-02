import re

password = input('Enter password: ')

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$'

if re.fullmatch(pattern , password):
    print("Valid password")
else:
    print("Invalid password") 
