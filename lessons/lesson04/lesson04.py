# for i in "text":
#     print(i)
# print("end script")
# a = 0
# while a < 10:
#     print(a)
#     a += 1

# while True:
#     pass

# print("end script")


# l = [1,2,3,4,5]
# while l:
#     print(f"remove {l.pop() =}")
#     print(l)
# else:
#     print ("The end")
# print("end script")

# print(list(range(5)))
# print(list(range(-5)))
# print(list(range(-10, -5)))
# print(list(range(-10, -50)))
# print(list(range(-10, -50, -1)))
# print(list(range(-10, -50, -10)))

# for i in range(5):
#     print(f"{i=}")

# l = [1,2,3, [10, 20,30]]
# # for i in l:
# #     print(f"{i=}", end=" => ")
# #     if type(i) is list:
# #         for e in range(10, 20, 2):
# #             i.append(e)

# #     i = i*2
# #     print(f"{i=}")
# # print(l)

# for i in range(len(l)):
#     print(f"l[{i}]={l[i]}", end= " => ")
#     l[i] = l[i]*2
#     print(f"l[{i}]={l[i]}")

# print(l)

# for i in range(1, 5):
#     N = 10 ** i
#     r = range(N)
#     l = list(r)
#     print(f"{N=}")
#     print(f"\t{r.__sizeof__() =}")
#     print(f"\t{l.__sizeof__() =}")

# l = enumerate("text")
# print(l, list(l))
# l = enumerate([10, 20, 30, 40, 50])
# print(l, list(l))
# for elemnt  in enumerate([10, 20, 30, 40, 50]):
#     print(f"{elemnt=}")


# a, b = 1,2
# a, b = (1,2)

# for index, value  in enumerate([10, 20, 30, 40, 50]):
#     print(f"{index=} {value=}")


# for i in "text":
#     print(f"{i}")
# for i in [1,2,3]:
#     print(f"{i}")
# for i in (1,2,3):
#     print(f"{i}")
# for i in set("qweewqewqewqewqe"):
#     print(f"{i}")

# d = {
#     "key1":1,
#     "key2":3,
#     "key3":3,
#      }
# for i in d:
#     print(f"{i} {d[i]}")
# for i in d.items():
#     print(f"{i}")
# for key, value in d.items():
#     print(f"{key} {value}")
# s = 0
# for i in range(10):
#     s += i
#     print(f"{i=} {s=}")
#     if s > 10:
#         break
# else:
#     print("end")
# print("end script")

# text = input("set text:")

# for c in text:
#     a = 1
#     if c == "1":
#         break
# else:
#     print("not contain ")


# print(a)

# s = 0
# for i in range(10):
#     s += i
#     print(f"{i=} {s=}")
#     if s % 2:
#         continue
#     print("text")
# else:
#     print("end")
# print("end script")

# for i in range(3):
#     print(f"{i=}")
#     for j in range(3):
#         print(f"\t{j=}")
#         for k in range(3):
#             print(f"\t\tf{k=}")

# for i in range(3):
#     print(f"{i=}")
#     for j in range(3):
#         print(f"\t{j=}")
#         if (i + j) % 2:
#             print("\tcontinue")
#             continue
#         for k in range(3):
#             print(f"\t\t{k=}")
#             if (i + j +k) > 3:
#                 print("\t\tbreak")
#                 break

# for i in "text":
#     pass
# def f():
#     pass


# for n in range(0, 101, 2):
#     print(n, end=" ")
# print()

# n = 0
# while n <= 100:
#     if n % 2 == 0:
#         print(n, end=" ")
#     n += 1
# print()

# a = range(100)
# for i in a:
#     if i % 2 == 0: 
#         print(n, end=" ")
# print()


# n = 0
# while n < 100:
#     if n % 2 == 0:
#         print(n)
#     n += 1
# # ------------------------------------------
# for n in range(0, 100):
#     if n % 2 == 0:
#         print(n)

# a = range(100)
# for i in a:
#     if i % 2 == 0:
#         continue
#     print(i)


# for n in range(101):
#     if not n%2:
#         continue
#     print(n)

# for n in range(1,101,2):
#     print(n)


# for i in range(1, 100): if i % 2 == 0: continue print(i)
#  #--------------------------------
# for i in range(1, 100): 
#     if i % 2 != 0:
#         print(i)

# a = [2,2,2,2,2,2,2,1421,5,6,5]
# for n in a:
#     if n%2:
#         print(n,"is odd")
#         break
#     print(n)
from random import randint
a = []
for i in range(10):
    a.append(randint(-10, 10))
print(a)
for n in a:
    if n%2:
        print(n,"is odd")
        break
    print(n)


list = [2, 4, 6, 8, 11]
odd = False
for n in list:
    if n % 2 !=0:
        odd = True
        break
if odd:
    print("founded odd")
else:
    print("no odd")