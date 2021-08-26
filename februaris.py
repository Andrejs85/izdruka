#1uzdevums

a = 15
b = 2.5
c = 4.78
if a>b and a>c:
    print("a ir lielākais skaitlis.")
elif b>a and b>c:
    print("b ir lielākais skaitlis.")
else:
    print("c ir lielākais skaitlis.")

#2uzdevums
x=float(input("Ievadi temperatūru: ")) 
if x<35:
    print("Vai nav par aukstu?")
elif x>=35 and x<=37: #35<=x<=37
    print("Viss kārtībā.")
else:
    print("Iespējams drudzis")

#risinajums ar list
myList=[a,b,c]
myList.sort()
print(f"Lielākais ir {myList[-1]}, bet mazakais skaitlis ir {myList[0]}.")

#
atr=input("Ievadi atrašanas vietu: ")
if atr=="bank":
    print("Te ir daudz naudas")
elif atr=="veikals":
    print("Jānopērk āboli")
elif atr=="aptieka":
    print("Man ir iesnas")
else:
    print("Ābolu nav")


