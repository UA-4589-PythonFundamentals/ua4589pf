import math
#task 1
def fun1 (a,b):
    if a>b:
        return a
    else :
        return b
f=float(input("веди число a="))
e=float(input("веди число b="))
print(fun1(f , e))    

#task 2
def rectrangle (l,w):
    return l * w

def triangle (O,h):
    return (O * h) / 2

def circle (R):
    return math.pi * R ** 2

CHOISE = input( 'Ведіть вашу фігуру ( rectrangle , triangle , circle )'  )

if CHOISE == "rectrangle" :
    l=int(input( 'ведіть Довжину' ))
    w=int(input( 'ведіть Штрину' ))
    print('Area:', rectrangle(l,w) )

elif CHOISE == "triangle" :
    o=int(input( 'ведіть Основу' ))
    h=int(input( 'ведіть Висоту' ))
    print('Area:', triangle(o,h))

elif CHOISE == "circle" :
    R=int(input( 'ведіть Радіус' ))
    print('Area:', circle(R) )

else:
    print("Не визначена фігура")


#task 3

def fun3 (s):
    result={}

    for i in s:
        result[i]=result.get(i,0)+1
    return result
    
print(fun3("hello"))    
    
    
    
    
    
