import re

password = input("your password: ")

# Conditions:
# 1. At least one lowercase letter [a-z]
# 2. At least one uppercase letter [A-Z]
# 3. At least one digit [0-9]
# 4. At least one special character from [$#@]
# 5. Length between 6 and 16 characters inclusive

if (6 <= len(password) <= 16 and
    re.search(r"[a-z]", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"\d", password) and
    re.search(r"[$#@]", password)):
    print("Valid password")
else:
    print("Invalid password")