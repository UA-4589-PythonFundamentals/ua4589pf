import re
pattern = input("Enter your password: ")
if re.findall("[A-Z]", pattern):
    if re.findall("[a-z]", pattern):
        if re.findall("[0-9]", pattern):
            if re.findall("[$#@]", pattern):
                if len(pattern) >= 6 and len(pattern) <= 16:
                    print("Valid Password")
                else:
                    print("Password length must be between 6 to 16 characters")
            else:
                print("Password must contain at least one special character from [$#@]")
        else:
            print("Password must contain at least one digit [0-9]")
    else:
        print("Password must contain at least one lowercase letter [a-z]")
else:
    print("Password must contain at least one uppercase letter [A-Z]")
