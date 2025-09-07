import math*
#task 1
    def greet (name):
        if name == "Johnny":
           return("Hello my love!")
        else:
            return"(Hello"+name+"!")

#task 2
    def distance (x,y,z,w):
        D=sqrt((x-z)**2+(y-w)**2)
        return round(D,2)

#task 3
    def my_str (txt):
       new_txt=txt.caseflod().capitalize() 
       return(new_txt)

#task 4
    def transform_num_str (num):
        return str(num)

#task 5
    def reserv_text (text):
        t=text.strip().split(" ")
        new_text=t[::-1]
        return " " join(new_text)

#tzsk 6
    def revers_list (list):
        new_list= list[::-1]
        return new_list

#task 7
    def sum_3_5 (N):
        s=0
        for i in range(N):
            if i%3 == 0 or i%5 == 0 :
                s+=i
                return s
            elif N<0 :
                return 0

#task 8
    def film_eckshin ( L,V,N ):
        """
        L - відстань яку треба проїхати
        V - затрати N на якусь певну відстань
        N - кількість нащого ходу який залишився 
        """
        return V * N >= L

#task 9
    def banjo (name):
        if neme[0] == R or name[0] == r :
            return (name +" plays banjo ")
        else :
            return (name + "does not play banjo")

#task 10
        def task10 (boolean):
            if boolean :
                return "Yes"
            else:
                return "No"

#task 11
    def count_sheep (Sheep):
        return sheep.count(True)

#task 12
    def correct_leter(body, tail):
        return body.endswith(tail)
    

        
    
            

        
