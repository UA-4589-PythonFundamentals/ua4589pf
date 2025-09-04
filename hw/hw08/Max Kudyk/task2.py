import re

def check_valid(password):
    errors = []

    if not (6 <= len(password) <= 16):
        errors.append("Password must include from 6 to 16 characters")

    if not re.search("[a-z]", password):
        errors.append("Password must include at least one lowercase character [a-z]")

    if not re.search("[A-Z]", password):
        errors.append("Password must include at least one uppercase character [A-Z]")

    if not re.search("[0-9]", password):
        errors.append("Password must include at least one digit [0-9]")

    if not re.search("[$#@]", password):
        errors.append("Password must include at least one special character [$#@]")

    if errors:
        for error in errors:
            print(error)
        return False

    return True


if __name__ == "__main__":
    user_password = input("Enter your password:\n")

    if check_valid(user_password):
        print("Valid password")
    else:
        print("Check errors")
