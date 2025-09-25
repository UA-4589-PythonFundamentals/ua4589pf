# # l = [i for i in range(1, 10) if i % 2 == 0]
# # print(l)
# # l = []
# # for i in range(1, 10):
# #     if i % 2 == 0:
# #         l.append(i)
# # print(l)
# # l = [j*i for i in range(1, 10) for j in "abcdef" if j in "ace" or i % 2 == 0]
# # print(l)
# # l = []
# # for i in range(1, 10):
# #     for j in "abcdef":
# #         if j in "ace" or i % 2 == 0:
# #             l.append(j*i)
# # print(l)


# import re


# l = {i: i**2 for i in range(1, 10) if i % 2 == 0}
# print(l)
# l = {i*j for i in range(1, 10) for j in range(1, 10)}
# print(l)

# l = (i for i in range(1, 10) if i % 2 == 0)
# print(l)
# # for i in l:
# #     print(i)
# # print("----")
# # for i in l:
# #     print(i)
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))
# # print(next(l))


# # for n in range(1, 7):
# #     l = [i for i in range(1, 10**n)]
# #     g = (i for i in range(1, 10**n))

# #     print(f"n = {n} list: {l.__sizeof__()}, gen: {g.__sizeof__()}")


# # l = [1,2,3,4,5]
# # t = "test"
# # print(zip(l, t))
# # print(list(zip(l, t)))
# # l = [1,2,3,4,5]
# # t = "test"
# # p = (10, 20, 30)
# # z = zip(l, t, p)

# # print(z)
# # for i in z:
# #     print(i)

# # add = lambda x, y: x + y
# # print(add(10, 20))

# # result = map(int, "123445")
# # print(result)
# # print(list(result))

# class Range:
#     def __init__(self, start, end=None, step=1):
#         print(f"init: {start=}, {end=}, {step=}")
#         if end is None:
#             self.end = start
#             self.start = 0
#         else:
#             self.start = start
#             self.end = end
#         self.step = step
#         self.current = None

#     def __iter__(self):
#         print(f"get iter: {self.start=}, {self.end=}, {self.step=}")
#         self.current = self.start
#         return self

#     def __next__(self):
#         print(f"next: {self.current=}, {self.end=}, {self.step=}")
#         if self.step > 0 and self.current >= self.end:
#             raise StopIteration
#         if self.step < 0 and self.current <= self.end:
#             raise StopIteration
#         i = self.current
#         self.current += self.step
#         return i
            
# print("----")        
# r = Range(5)
# for i in r:
#     print(i, end=" ")
# print("----")
# r = Range(5, 20, 2)
# for i in r:
#     print(i, end=" ")
# print("----")
# r = Range(5, 10)
# for i in r:
#     print(i, end=" ")
# print("----")
# r = Range(10, 5, -1)
# itr = iter(r)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# try:
#     print(next(itr))
# except StopIteration:
#     print("End of iteration")
# print("----")

# print(list(Range(5)))



# # list

# # T = int | float | str
# # def f(n: T) -> int:
# #     if n <= 1:
# #         return 1
# #     return n * f(n-1)

# def f(n: int) -> int:
#     print(f"call f({n})")
#     return n**n
# print(f)
# print(f(5))
# def f(n: int) -> int:
#     print(f"call f({n})")
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# print(f)
# g = f(5)
# print(f"g: {g}")
# print("----")
# print(next(g))
# print("----")
# print(next(g))
# print("----")
# print(next(g))
# print("----")
# print(next(g))
# print(next(g))
# print(next(g))


def select_all_users():
    # sql = "SELECT * FROM users"
    sql = """
    SELECT * FROM users
    ORDER BY id DESC
    LIMIT {limit}
    OFFSET {offset}
    """
    limit = 5
    offset = 0
    while True:
        print(f"exec sql: {sql.format(limit=limit, offset=offset)}")
        # rows = db.execute(sql.format(limit=limit, offset=offset))
        rows = [{"id": i, "name": f"user{i}"} for i in range(offset+1, offset+limit+1)]
        if not rows:
            break
        for row in rows:
            yield row
        offset += limit

g = select_all_users()
print(g)
for _ in range(25):
    print("----")
    print(next(g))

