# def add(a):
#     print("In decorator")
#     return a
# print(add(10))


# @add
# def print_info(func):
#     print(f"Function name: {func.__name__}")

# def decorator(func):


#     def wrapper(*args, **kwargs):
#         # print(f"Before function call {func.__name__} with args: {args} and kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         # print(f"After function call {func.__name__} returned: {result}")
#         return result
    
#     return wrapper

# def add(a, b):
#     return a + b
# add = decorator(add)

# @decorator
# def multiply(a, b):
#     return a * b

# print(f"{add(10, 20) =}")
# print(f"{add(a=300, b=200) =}")
# print(f"{multiply(10, 20) =}")
# print(f"{multiply(a=300, b=200) =}")

# def before_after_char(char, count=10):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(char * count)
#             result = func(*args, **kwargs)
#             if func.__name__ != "wrapper":
#                 print(f"{func.__name__} returned {result}")
#             print(char * count)
#             return result
#         return wrapper
#     return decorator



# @before_after_char(char="=", count=10)
# @before_after_char(char=">", count=10)
# @before_after_char(char="<=", count=10)
# def div(a, b):
#     return a / b

# print(f"{div(10, 2) =}")

functions = {}

def parameterized(*types):
    def decorator(func):
        functions[types] = func
        def wrapper(*args):
            t = [type(a) for a in args]
            f = functions.get(tuple(t))
            result = f(*args) if f else None
            return result
        return wrapper
    return decorator
# def parameterized(*types):
#     def decorator(func):
#         t = sorted(types, key=lambda x: x.__name__)
#         functions[tuple(t)] = func
#         def wrapper(*args):
#             t = sorted(map(type, args), key=lambda x: x.__name__)
#             print(t)
#             f = functions.get(tuple(t))
#             result = f(*args) if f else None
#             return result
#         return wrapper
#     return decorator
@parameterized(int, int)
def add(a, b):
    return a + b

@parameterized(str, int)
def add(a, b):
    return a * b
@parameterized(int, str)
def add(a, b):
    return "!\t" + str(a * b) + "!"

@parameterized(str, str)
def add(a, b):
    return a + b + "!"

print(add(140, 204))
print(add("Hello", 9))
print(add("Hello", "World"))
print(add(10, 20))
print(add("Hello", 3))
print(add("Hello ", "World"))



print(add(10, "World"))
print(add("World",5))

from pprint import pprint
pprint(functions)