#TASK 1

def largest_of_two(num1, num2):
    """
    Takes two numbers and checks what's bigger
    """
    if num1 == num2:
        print(f"{num1} and {num2} are equal")
        return num1, num2
    elif num1 > num2:
        print(f"{num1} is bigger than {num2}")
        return num1
    else:
        print(f"{num2} is bigger than {num1}")
        return num2

# a = largest_of_two(1,1)
# b = largest_of_two(2,10)
# c = largest_of_two(-1412421421421,-42314234234141241432)

# print(a,b,c,sep="<=>")

