
# # file = open("lessons/lesson14/myfile.txt", "r")
# # # text = file.read(3)
# # # print(text)
# # # print("-----")
# # # text = file.read()
# # # print(text)

# # # for line in file:
# # #     print("-", line.strip())

# # # while True:
# # #     line = file.readline()
# # #     if not line:
# # #         break
# # #     print("--", line.strip())

# # # l = file.readline()
# # # print(file.tell())
# # # ll = file.readlines()
# # # print(l)

# # # print(ll)
# # # print(file.tell())

# # print(f"file.tell(): {file.tell()}")
# # for line in file:
# #     print(line.strip())
# #     # print(f"file.tell(): {file.tell()}")

# # print(f"file.tell(): {file.tell()}")
# # file.seek(1)
# # print(f"file.tell(): {file.tell()}")
# # for line in file:
# #     print(line.strip())
# #     # print(f"file.tell(): {file.tell()}")

# # file.close()

# # with open("lessons/lesson14/myfile.txt", "r") as file:
# #     for line in file:
# #         print(line.strip())

# #     print(f"file.tell(): {file.tell()}")
# import csv
# with open("lessons/lesson14/data.csv", "r", encoding="utf-8") as file:
#     # reader = csv.reader(file)

#     # header = next(reader)
#     # print(header)
#     # for row in reader:
#     #     print(dict(zip(header, row)))  
#     # 
#     dict_reader = csv.DictReader(file)
#     for row in dict_reader:
#         print(row)
#         print(row["name"], row["age"], row["city"]) 
# # with open("lessons/lesson14/myfile.txt", "a", encoding="utf-8") as file:
# #     file.write("\nline4")
# #     file.write("\nline5")
# #     file.write("\nline6")
# #     file.writelines(["\nline7", "\nline8", "\nline9"])