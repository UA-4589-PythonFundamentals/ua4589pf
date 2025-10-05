import re


def check_password(text):
    if len(text) < 6 or len(text)>16:
        return False

    if not re.search(r"[a-z]",text):
        return False

    if not re.search(r"[A-Z]",text):
        return False
    
    if not re.search(r"[@#$]",text):
        return False
    
    if not re.search(r"[\d]",text):
        return False
    
    return True


password = input("Enter your password: ")

print(check_password(password))