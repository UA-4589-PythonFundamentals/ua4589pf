def larg_num(num1: int, num2: int):
    """
    Returns the largest of two numbers.
    """
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Numbers are equal"