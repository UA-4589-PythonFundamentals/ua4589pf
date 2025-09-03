import geometry

print("Що ви хочете обчислити?")
print("1 - Площа прямокутника")
print("2 - Площа трикутника")
print("3 - Площа кола")

choice = input("Введіть номер вибору: ")

if choice == "1":
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    print("Площа прямокутника:", geometry.area_rectangle(a, b))

elif choice == "2":
    base = float(input("Введіть основу: "))
    height = float(input("Введіть висоту: "))
    print("Площа трикутника:", geometry.area_triangle(base, height))

elif choice == "3":
    r = float(input("Введіть радіус: "))
    print("Площа кола:", geometry.area_circle(r))

else:
    print("Некоректний вибір!")