def passCheacker(password):
    spec = '$#@'
    
    if len(password) < 8:
        return "Password invalid. Length too short"
    elif len( password) > 16:
        return "Password invalid. Length too long"
    
    lower = any(ch.islower() for ch in password)
    upper = any(ch.isupper() for ch in password)
    digit = any(ch.isdigit() for ch in password)
    special = any(ch in spec for ch in password)

    if not(lower):
        return "Add at least 1 lowercase letter [a-z]"
    elif not(upper):
        return "Add at least 1 uppercase letter [A-Z]"
    elif not(digit):
        return "Add at least 1 digit [0-9]"
    elif not(special):
        return "Add at least 1 special char from [$#@]"
    else:
        return "Password is valid"
