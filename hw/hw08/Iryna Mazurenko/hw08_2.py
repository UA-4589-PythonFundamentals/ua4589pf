def is_valid_password(password):

    if not (6 <= len(password) <= 16):
        return False

    has_lower   = any(c.islower() for c in password)
    has_upper   = any(c.isupper() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_special = any(c in "$#@" for c in password)

    return has_lower and has_upper and has_digit and has_special

# --- Main program ---
try:
    user_pass = input("Enter password: ")
except EOFError:
    print("Input error: No input provided.")
    exit(1)

print("Valid password" if is_valid_password(user_pass) else "Invalid password")


