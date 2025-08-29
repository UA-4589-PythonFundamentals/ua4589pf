# def my_function():
#     """
#     This is a docstring for my_function.
#     """
#     print("Hello from my_function!")
# print(my_function)
# m = my_function
# print(m)
# print(my_function.__doc__)
# help(my_function)
# print(f"{my_function()=}")
# def print_name(name):
#     """
#     This is a docstring for print_name.
#     """
#     print(f"Hello, {name}!")

# print_name("Alice")
# print_name("Bob")


# def absolute_value(num):
#     """
#     This function returns the absolute value of a number.
#     """
#     if type(num) in (int, float):
#         if num < 0:
#             return -num
#         return num
#     print("Error: Input must be an integer or float.")
# print(f"{absolute_value(-5)=}")
# print(f"{absolute_value(3)=}")
# print(f"{absolute_value('3')=}")

# f = lambda x: x * x
# print(f(5))

# def print_user_info(name, age, city):
#     """
#     This function prints the user's name and age.
#     """
#     print(f"Name: {name}, Age: {age}, City: {city}")

# def print_user_info(name: str, age: int, city: str) -> None:
#     """
#     This function prints the user's name and age.
#     """
#     print(f"Name: {name}, Age: {age}, City: {city}")

# print_user_info("Alice", 30, "New York")
# print_user_info("Alice", 30) #TypeError: print_user_info() missing 1 required positional argument: 'city'
# print_user_info("Alice", 30, "Los Angeles", "temp") #TypeError: print_user_info() takes 3 positional arguments but 4 were given

# print_user_info(10, "30", 10)


# def print_user_info(name, age=18, city1="Unknown"):
#     """
#     This function prints the user's name and age.
#     """
#     print(f"Name: {name}, Age: {age}, City: {city1}")

# print_user_info("Alice")
# print_user_info("Alice", 30)
# print_user_info("Alice", 30, "Los Angeles")
# print_user_info("Alice", 30, "Los Angeles", 1)#TypeError: print_user_info() takes from 1 to 3 positional arguments but 4 were given
# print_user_info()#TypeError: print_user_info() missing 1 required positional argument: 'name'
# print_user_info("Los Angeles", "Alice", 30)
# print_user_info(city1="Los Angeles", name="Alice", age=30)


# def sum_numbers(*args, **kwargs):
#     """
#     This function returns the sum of two numbers.
#     """
#     print(f"{args=}")
#     print(f"{kwargs=}")
#     return sum(args) + sum(kwargs.values())
# print(sum_numbers(1, 2))
# print(sum_numbers(1, 2, 3, 4, 5))
# print(sum_numbers())
# print(sum_numbers(1,2,3,4, a=1, b=2))

# def func(a, b, *args, d=1, c=2, **kwargs):
#     """
#     This function takes multiple arguments and keyword arguments.
#     """
#     print(f"{a=}, {b=}, {args=}, {d=}, {c=}, {kwargs=}")

# func(1, 2)
# func(1, 2, 3, 4, 5)
# func(1, 2, 3, 4, 5, d=10, c=20, e=30)
# func(1, 2, 3, 4, 5, a=10, d=10, c=20, e=30) #TypeError: func() got multiple values for argument 'a'
# func(1, a=2, 3, 4, 5, d=10, c=20, e=30)#SyntaxError: positional argument follows keyword argument
# def my_print_str(*args, sep=" ", end="\n"):

#     result = sep.join(map(str, args)) + end
#     print(result)
#     return result
# s = my_print_str(1, 2, 3, 4, 5)
# s += my_print_str(1, 2, 3, 4, 5, sep=", ", end="!")
# s +=my_print_str(1, 2, 3, 4, 5, sep=", ", end="!")
# print(s)


# def function_add_one(lst=[]):
#     lst.append(1)
#     print(lst)
# def function_add_one(lst=None):
#     if lst is None:
#         lst = []
#     lst.append(1)
#     print(lst)


# function_add_one()
# function_add_one([1, 2, 3])
# function_add_one()
# function_add_one([4, 5, 6])
# function_add_one()

# def f():
#     a = 10
#     print(f"Inside f: {a=}")
# f()
# print(f"Outside f: {a=}") #NameError: name 'a' is not defined
# count = 0

# def info_count():
#     print(f"{count=}")
# info_count()
# count += 1
# info_count()
# del count
# info_count() #NameError: name 'count' is not defined. Did you mean: 'round'?


count = 0

def info_count():
    # print(f"{count=}") #UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    # count = 0
    count = 1
    print(f"{count=}")


# info_count()
# print(f"g_{count=}")

# count = 0

# def info_count():
#     global count
#     print(f"{count=}") #UnboundLocalError: cannot access local variable 'count' where it is not associated with a value

#     count += 1
#     print(f"{count=}")


# info_count()
# print(f"g_{count=}")


# l = []
# def l2():
#     l.append(2)
#     print(f"{l=}")
# # def l2(l):
# #     l.append(2)
# #     print(f"{l=}")

# l2()
# l2()
# l2()
# print(f"{l=}")

# class MyClass:
#     def __init__(self):
#         print(f"\tMyClass instance is created {id(self)=}")
        
#     def __del__(self):
#         print(f"\tMyClass instance is being deleted {id(self)=}")

# m = MyClass()


# def create_instance():
#     ins = MyClass()
#     return ins
# print("run function1")
# create_instance()
# print("end function1")
# print("run function2")
# i = create_instance()
# print("end function2")
# print("end script")


# def create_instance(num):
#     my_num = num
#     def create():
#         print(f"{my_num=}")
#     return create

# a10 = create_instance(10)
# a20 = create_instance(20)

# a10()
# a20()
# a10()
# a20()


# g = "global variable"

# def create_instance():
#     nonlocal g # SyntaxError: no binding for nonlocal 'g' found
#     g = "local variable"
#     def create():
#         nonlocal g
#         g = "inner variable"
#         print(f"create {g=}")
#     print(f"create_instance {g=}")
#     return create

# a = create_instance()
# a()
# print(f"{g=}")


# def factorial(n, level=0, line=""):
#     if n == 0:
#         # print(f"{'  ' * level}{line}1")
#         return 1
#     else:
#         # print(f"{'  ' * level}{line}factorial({n})")
#         line += f"{n}*"
#         return n * factorial(n-1, level+1, line)

# print(f"{factorial(5)=}")
# import sys
# sys.setrecursionlimit(6000)
# sys.set_int_max_str_digits(60000)
# print(f"{factorial(5000)=}")

# l = ["1", 10, 3.14,"test", -5, None, [1,2,3], (4,5,6), {7,8,9}, {"a":1, "b":2}]

# for item in l:
#     print(f"{item}: {type(item)}")
# # l.sort() #TypeError: '<' not supported between instances of 'int' and 'str'

# l.sort(key=str)
# print(l)

# def el(element):
#     if element is None:
#         return 0
#     elif isinstance(element, (int, float)):
#         return element
#     elif isinstance(element, str):
#         return len(element)
#     else:
#         return 100
# lam = lambda x: 0 if x is None else x if isinstance(x, (int, float)) else len(x) if isinstance(x, str) else 100
# l.sort(key=el)
# print(l)
# l.sort(key=lambda x: x if isinstance(x, (int, float)) else 0)
# print(l)


def print_user_info(name, age, city):
    """
    This function prints the user's name and age.
    """
    return f"Name: {name}, Age: {age}, City: {city}"

pui = lambda name, age, city: f"Name: {name}, Age: {age}, City: {city}"

print(print_user_info("Alice", 30, "New York") == pui("Alice", 30, "New York"))