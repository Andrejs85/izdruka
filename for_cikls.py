#iteracija - kadas darbibas atkartota izpildišana
mainigais=[1,2,3]
for elements in mainigais:
    print(elements) #darbibas kas javeic

#izdruka list elementus
myList=[1,2,3,4,5,6,7,8,9,10,11,12]
for sk in myList:
    print(sk)

for _ in myList:
    print("Sveiki!") #var nerakstit cikla mainiga nosaukumu

#izdruka tikai parra  skaitļus
for sk in myList:
    if sk%2==0:
        print(sk)
    else:
        print(f"{sk} ir nepara skaitlis")

#summas apreķinašana
myList=[1,2,3,4,5,6,7,8,9,10,11]
summa=0

for sk in myList:
    summa=summa+sk
    print(f"Pēc {sk} skaitļu saskaitišanas summa ir {summa}")
    
print(summa)

#drukā tekstu
myString="Sveika, pasaue!"
for burts in myString:
    print(burts)

for burts in "programma":
    print(burts, end=" ")

#druka tuple
tup=(1,2,3,4)
for elements in tup:
    print(elements)

myList=[(1,2), (3,4), (5,6), (7,8)] #packed tuple
print(len(myList))

for elements in myList:
    print(elements)

for viens,otrs in myList: #var nelikt iekavas
    print(viens)
    print(otrs)

myList=[(1,2,3), (4,5,6), (7,8,9)]
for a,b,c in myList:
    print(b)

#vardnicas 
d={"k1":11, "k2":12, "k3":13}
for elements in d:
    print(elements) #izdruka tikai atslegas

for elements in d.items():
    print(elements) #drukā pārus

for atslega, vertiba in d.items():
    print(vertiba)
    print(atslega)

#Given an Integer N, print all the numbers from1 to N.

#ar skaitļiem izmanto funkciju range()

for skaitlis in range(15): #izdruka visus skaitļus no [0;15)
    print(skaitlis)

for skaitlis in range(5, 15): #izdruka visus skaitļus no [5;15)
    print(skaitlis)

for skaitlis in range(5,15,2): #izdruka visus skaitļus no [0;15) ar soli 2
    print(skaitlis)