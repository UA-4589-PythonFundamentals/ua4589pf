# a = 1
# b = 2

# print(a>b)
# print(a<b)
# a = "21"
# b = "2"

# print(a>b)
# print(a<b)
# a = ["21"]
# b = ["2"]

# print(a>b)
# print(a<b)
# a = ["21"]
# b = 1

# # print(a>b)#TypeError: '>' not supported between instances of 'list' and 'int'
# # print(a<b)#TypeError: '>' not supported between instances of 'list' and 'int'

# a = int(input("a:"))
# print(a >=18 and a <=65)
# print(18 <= a <= 65)
# print(a< b and b < c and c < d)
# print(a< b < c <d)
# print(89 and [1,2,3])
# print(89 and [1,2,3] and 0 and "sfds")
# print(0 or None or 10 or "test" or "")
# print(0 or None  or "" or [])
# is_false = [False, None, 0, 0.0, "", [], (), {}]

# if len(l) > 0:
#     pass
# if l:
#     pass

# l1 = [1,2,3]
# l2 = [1,2,3]
# l12 = l1
# print(f"{l1 is l2=}")
# print(f"{l1 is l12=}")
# print(f"{l2 is l12=}")
# print(f"{l2 is not l12=}")

# l = [1,2,3, [4,5], "test"]
# print(f"{1 in l =}")
# print(f"{4 in l =}")
# print(f"{[4,5] in l =}")
# print(f"{"t" in l =}")
# print(f"{"test" in l =}")
# print(f"{"es" in "test" =}")
# print(f"{"es" not in "test" =}")
# # print(f"{"es" not in 1 =}") #TypeError: argument of type 'int' is not iterable



# score = int(input("score:"))
# if score > 8:
#     print("start if true")
#     print("You have passed the exam")
#     print("end if true")


# print("Exam was finished.")

# temperature = float(input('What is the temperature? '))
# if temperature > 30:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')
# print('Get some exercise outside.')

# score = int(input("score:"))
# if score >= 90:
#     letter = 'A'
# else:
#     # grade must be B, C, D or F
#     if score >= 80:
#         letter = 'B'
#     else: # grade must be C, D or F
#         if score >= 70:
#             letter = 'C'
#         else: # grade must D or F
#             if score >= 60:
#                 letter = 'D'
#             else:
#                 if score >= 50:
#                     letter = 'E'
#                 else:
#                     letter = 'F'

# print(letter)

# if score >= 90:
#     letter = 'A'
# elif score >= 80:
#     letter = 'B'
# elif score >= 70:
#     letter = 'C'
# elif score >= 60:
#     letter = 'D'
# elif score >= 50:
#     letter = 'E'
# else:
#     letter = 'F'

# print(letter)

# l = [1,2,3, [4,5], "test"]

# for i in l:
#     if type(i) is list:
#         print(i)

# weather = "raining"

# if weather == "raining":
#     text = "Open Your umbrella"
# else:
#     text = "Wear your cap"
# print(text)

# text = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# # text = weather == "raining" ? "Open Your umbrella" : "Wear your cap"
# print(text)

# status = int(input("statuss code:"))

# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
# match status:
#     case 400:
#         print("Bad request")
#     case 401 | 403  as code:
#         print(f'{code} is authentication error')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
# values = input("line:")
# values = values.split()
# print(f"{values =}")
# match values:
#     case "load", link:
#         print(link)
#     case "save", link, filename:
#         print("save")
#         print(f"\t{link}, {filename}")
#     case "save", link, *filenames:
#         print(f"save: {link}")
#         for filename in filenames:
#             print(f"\t{filename}")
#     case _:
#         print(values)

# t = (
#     ["evening", "run"],
#     ["all","sleep"],
#     [1,2,3,4],
#     "text",
# )
# for item in t:
#     match item:
#         case ['evening', action]:
#             print(f'You almost finished the day! Now {action}!')    
#         case [time, action]:
#             print(f'Good {time}! It is time to {action}!')
#         case _:
#             print('The time is invalid.')

# t = (
#     {"time":"evening", "action":"run"},
#     {"time":"evening", "action":"run", "city": "Lviv"},
#     {"time":"all", "action":"sleep"},
#     {"time":"all", "city": "Lviv"},
#     ["all","sleep"],
#     [1,2,3,4],
#     "text",
# )
# for item in t:
#     print(item, end=" => ")
#     match item:
#         case {"time": 'evening', "action": action}:
#             print(f'You almost finished the day! Now {action}!')
#         case {'time': time, 'action': action}:
#             print(f'Good {time}! It is time to {action}!')
#         case _:
#             print('The time is invalid.')

def f400():
    print("Bad request")
d = {
    400: f400,
    401: lambda : print("Unauthorized")
}

status = int(input("statuss code:"))
try:
    d[status]()
except:
    print("Other error")