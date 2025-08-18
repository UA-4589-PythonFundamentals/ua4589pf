# list

# l = list()
# print(type(l), l)
# # l = list(1, 2, 3)#TypeError: list expected at most 1 argument, got 3
# # l = list(1) #TypeError: 'int' object is not iterable
# l = list([1, 2, 3])
# print(type(l), l)
# l = list("text")
# print(type(l), l)
# l = []
# print(type(l), l)
# l = [1, "text", 2.5, [1,23], (1, 2)]
# print(type(l), l)

# l = [1, "text", 2.5, [1,23], (1, 2)]
# print(l[0])
# print(l[1][1])
# print(l[2])
# print(l[3], l[3][0], l[3][1])
# print(l[4])
# l.append(l)
# print(l)
# print(f"{l[-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1][-1]} =")
# l[0] = 100
# print(l) 
# print(l[1:5]) 
# print(l[2::2]) 
# print(l[::]) 
# print([1,2,3]+[4,5,6])
# print([1,2,3]*3)
# l = [1, "text", 2.5, [1,23], (1, 2)]
# print(f'{1 in l=}')
# print(f'{"text" in l=}')
# print(f'{"t" in l=}')
# print(f'{"t" in l[1]=}')
# print(f'{2.5 in l=}')
# print(f'{[1,23] in l=}')
# print(f'{(1, 2) in l=}')

# print([1,2,3] == [1,2,3])
# print([1,2,3] == [1,3,2])
# print([1,2,3] == [1,2,4])
# print([1,2,3] == [1,2,3,4])
# print([1,2,3] == (1,2,3))

# print([method for method in dir(list) if not method.startswith("__")])
# a = []
# a.append(1)
# a.append("text")
# a.append("text")
# a.append([1, 2, 3])
# print(a)
# a.extend([4, 5, 6])
# print(a)
# a.insert(1, "inserted")
# print(a)
# result = a.remove("text")
# # a.remove("1text") #ValueError: list.remove(x): x not in list
# print(result, a)
# result = a.pop()
# print(result, a)
# result = a.pop(0)
# print(result, a)
# a = [1,2,3,4,1,2,3,4,5,1,2,3,4, "text", "text", [1, 2, 3]]
# print(a)
# i = a.index(1)
# print(i)
# i = a.index(1, i + 1)
# print(i)
# i = a.index(1, len(a) - 1)#ValueError: 1 is not in list
# i = a.index(1, i + 1)
# print(i)
# i = a.index(1, i + 1, 8)
# print(a.count(1))
# print(a.count("text"))
# print(a.count([1,2,3]))
# a = [1,2,3]
# print(id(a), a)
# a.clear()
# print(id(a), a)
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9, a, b]
# print(c)
# print(id(c[3]) == id(a))
# print(c[4] is b)
# a.clear()
# b = []
# print(a, b)
# print(c)
# print(id(c[3]) == id(a))
# print(c[4] is b)

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9, a, b]
# d = c.copy()
# print(c, d)
# a[0] = 100
# c[0] = 200
# c[3][2] = 300
# print(a, b)
# print(c)
# print(d)
# import copy
# dd = copy.deepcopy(c)
# print(c, d)
# a[0] = 99
# c[0] = 85
# c[3][2] = 73
# print(a, b)
# print(c)
# print(d)
# print(dd)


# l = [1,2,4,2,3,5,7,8,43,3,21]
# print(l)
# l.reverse()
# print(l)
# l.sort()
# print(l)
# l = [1, "a5",2,"4",]
# # l.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'
# l.sort(key=lambda x: str(x))  # Sorts by string representation
# print(l)

# a = [1,3,1,5,2,4]
# print(sorted(a))  # Returns a new sorted list
# print(a)  # Original list remains unchanged

# matrix = [[i, j] for i in range(3) for j in range(3) if i != j]
# print(matrix)
# matrix = []
# for i in range(3):
#     for j in range(3):
#         if i != j:
#             matrix.append([i, j])

# tuple
# t = tuple()
# print(type(t), t)
# t = tuple([1, 2, 3])
# print(type(t), t)
# t = ()
# print(type(t), t)
# t = (1,2,3)
# print(type(t), t)
# t = (1)
# print(type(t), t)
# t = (1,)
# print(type(t), t)
# print([method for method in dir(tuple) if not method.startswith("__")])
# t = (1, 2, 3, [4, 5, 6])
# print(t)
# print(t[0])
# print(t[3])
# # t[0] = 100 # TypeError: 'tuple' object does not support item assignment
# t[3][0] = 100  # This is allowed because the list inside the tuple is mutable
# print(t)

# for n in range(1,10):
#     print(f"{n=}")
#     l = [e for e in range(n**2)]
#     t = (e for e in range(n))
#     print(f"\t{l.__sizeof__()=} {l[:15]=}")
#     print(f"\t{t.__sizeof__()=} {t=}")

#set

# s = set()
# print(type(s), s)
# s = set([1, 2, 3,1,3,2,1])
# print(type(s), s)
# s = set("dshbfhsdvhgsafdhgsafdhgsafdhgsafdhgds")
# print(type(s), s)
# s = {}
# print(type(s), s)
# s = {1,2,1,2,1,2}
# print(type(s), s)
# list 
# print([method for method in dir(set) if not method.startswith("__")])

# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(3)
# print(s)
# print(s.pop())
# print(s.remove(2))
# print(s)
# print(s.update([1,2,3]))
# print(s)

# # print(set("hsdfhdsbfjbgfdbghbsdbgjk"))


#dict 

# d = dict()
# print(type(d), d)
# d  = dict([(1, 'a'), (2, 'b'), (3, 'c')])
# # d  = dict([(1, 'a'), (2, 'b'), (3, 'c', 3)])#ValueError: dictionary update sequence element #2 has length 3; 2 is required
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {
#     11: 'a',
#     "2": 'b',
#     (22, 3): 'c'
# }
# print(type(d), d)
# print(d[11])
# print(d["2"])
# print(d[(22, 3)])
# d["42424"] = 12
# d[11] = 13
# print(d)
# d["text"] #KeyError: 'text'


print([method for method in dir(dict) if not method.startswith("__")])
d = {
    11: 'a',
    "2": 'b',
    (22, 3): 'c'
}
# print(d.get(11))
# print(d.get("text"))
# print(d.get(11, 100))
# print(d.get("text", 100))
# print(d.pop(11))
# print(d.pop(11, 100))  # Returns 100 if key 11 is not found
# print(d.popitem())  # Returns 100 if key 11 is not found
# print(d)
d.update({1: "one", 2: "two"})
print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for key in d:
#     print(f"{key} -> {d[key]}")
# a,b = (2,3)
# print(a, b)
# for key, value in d.items():
#     print(f"{key} -> {value}")
dd = d.fromkeys([1, 2, 3], "default")
print(dd)

sorted_dict = dict(sorted(d.items(), key=lambda item: str(item[0])))
print(sorted_dict)
