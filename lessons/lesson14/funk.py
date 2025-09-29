

def quadratic(a, b, c):
    """Return the roots of the quadratic equation ax^2 + bx + c = 0."""
    d = b**2 - 4*a*c  # discriminant
    if d < 0:
        return None  # No real roots
    elif d == 0:
        x = -b / (2*a)
        return x  # One real root
    else:
        sqrt_d = d**0.5
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        return (x1, x2)  # Two real roots