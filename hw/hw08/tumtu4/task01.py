import re

def valid_pattern_password(pattern: str, password: str) -> str | None:
    comp = re.compile(pattern)
    result = comp.search(password)
    if result == None:
        return f'Write 1 letter between {pattern}'


password = input("Enter your password: ")
patterns = ["[a-z]", "[A-Z]", "[0-9]", "[$#@]"]
for pattern in patterns:
    problem = valid_pattern_password(pattern,password)
    if problem:
        print(problem)

min_len = 6
max_len = 16
if not(min_len<len(password)<max_len):
    print("Password must have a length between 6 to 16 ch!")