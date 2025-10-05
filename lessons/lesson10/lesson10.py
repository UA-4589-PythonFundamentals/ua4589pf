# print (type(list), list)
# l = [1, 2, 3, 4, 5]
# print(type(l), l)


# class MyClass:
#     """MyClass docstring"""
#     pass

# print(type(MyClass), MyClass)
# obj = MyClass()
# print(type(obj), obj)
# print(type(obj) == MyClass)

# class Temp:
#     cm = ["a", "b", "c"]
#     ci = 0
#     def __init__(self):
#         self.im = [1, 2, 3]
#         self.ii = 100
#     def print_info(self):
#         print(self.cm, self.ci, self.im, self.ii)
# t = Temp()
# t2 = Temp()
# print(type(t), t)
# print(t.cm, t.ci, t.im, t.ii)
# print(t2.cm, t2.ci, t2.im, t2.ii)
# t.im.append(4)
# t2.im.append(50)
# t.ii += 1
# t2.ii += 20
# t.cm.append("d")

# print(t.cm, t.ci, t.im, t.ii)
# print(t2.cm, t2.ci, t2.im, t2.ii)
# # print(dir(t))
# print(Temp.__dict__)
# print(t.__dict__)
# print(t2.__dict__)

# t.print_info()
# t2.print_info()

# f = Temp.print_info
# f(t)
# print(type(Temp.print_info))
# print(type(t.print_info))
# print(type(f))