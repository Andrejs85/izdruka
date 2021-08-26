"""
#funkcija atgriež 10% no a un 20% no skaitļa b
def procenti(a, b):
    return a*10/100, b*0.20

print(procenti(100,1000))

#Uzraksti funkciju var_pagulet, kas atgriež True, ja ir brīvdiena un False, ja ir darbdiena.

def var_pagulet(diena):
    if  diena==brivdiena:
        return True
    else:
        return False

print(var_pagulet("brivdiena"))

#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble. Funkcija ir_problema

def ir_problema(a_smile,b_smile):
    if a_smile==b_smile:
        return True
    else:
        return False
print(ir_problema(True,False))

#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def summa(sk1, sk2):
    if sk1+sk2:
        return (sk1+sk2)*2
    return sk1+sk2
    
print(summa(3,2))
"""
#Dots pozitivs veselais skaitlis n. Uzraksti funkciju, kas atgriež starpības moduli starp n un 21, izņemot, ja modulis ir vairāk nekā 21, tad atgriež dubultu tā vērtību.



def starpiba (n):
    if n<=21:
        st=21-n
    else:
        st=n-21
    if st>21:
        return st*2
    return st

print(starpiba(3))
print(starpiba(45))

#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble. Funkcija papagaila_problema

def papagaila_problema(hour, runa):
    if (hour<7 or hour>20) and runa==True:
        return "we are in trouble"
    else:
        return "we are not in trouble"

print(papagaila_problema(13, True))

