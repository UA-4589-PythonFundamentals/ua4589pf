from area import area_circle as ac, area_rectangle as ar, area_triangle as at

number = int(input("1-коло\n2-прямокутник\n3-трикутник\nПлощу, якої фігури ви хочете обчислити:"))

match number:
    case 1:
        r = float(input("Введіть радіус:"))
        print(ac(r))
    case 2:
        a = float(input("Введіть першу сторону:"))
        b = float(input("Введіть другу сторону:"))
        print(ar(a, b))
    case 3:
        a = float(input("Введіть сторону:"))
        h = float(input("Введіть висоту:"))
        print(at(a, h))
    case _:
        print("Error...")