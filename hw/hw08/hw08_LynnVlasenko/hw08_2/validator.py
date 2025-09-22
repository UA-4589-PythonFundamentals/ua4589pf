import re

# the rules to check the password
RULES = [
    (lambda password: 6 <= len(password) <= 16, "! Length must be between 6 and 16 characters."),
    (lambda password: re.search(r"[a-z]", password), "! Must contain at least one lowercase letter [a-z]."),
    (lambda password: re.search(r"[A-Z]", password), "! Must contain at least one uppercase letter [A-Z]."),
    (lambda password: re.search(r"[0-9]", password), "! Must contain at least one digit [0-9]."),
    (lambda password: re.search(r"[$#@]", password), "! Must contain at least one special character from [$#@]."),
]

def check_password(password):
    """Function to checks the password for compliance with the rules - returns a list of errors."""
    return [text for rule, text in RULES if not rule(password)]