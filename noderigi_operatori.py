#vienkarši piepildit list ar elementiem
saraksts=list(range(0,11,2))
print(saraksts)

#enumerate - parada indeksus tuple formā
vards="pasaule"
for i in enumerate(vards):
    print(i)
#atpakojot tuples
vards="pasaule"
for indekss,burts in enumerate(vards):
    print(indekss)
    print(burts)
    print("\n")

#izmanto zip - sapako vairākus list kopā kā tuple
mylist1=[1,2,3]
mylist2=["a", "b", "c"]
for i in zip(mylist1, mylist2):
    print(i)

mylist3=[100,200,300,400]
for i in zip(mylist1, mylist2, mylist3):
    print(i)

#ja kada no list ir vairak elementu, rezultats bus tas pats, jo zip paņem tik, cik mazakajā

#izmanto in, lai noskaidrotu vai objektā atrodams mekletais elements
print("x" in [1,2,3])
print(2 in [1,2,3])
print("a" in "pasaule")
print("mykey" in {"mykey":345})
d={"mykey":345}
print(345 in d.keys())
print(345 in d.values())

#min un max
mylist=[10,20,30,40,100]
print(min(mylist))
print(max(mylist))

#biblioteku importešana
#random - nejaušs, gadījums skaitlis
from random import shuffle 
mylist=[1,2,3,4,5,6,7,8,9,10]
print(mylist)
shuffle(mylist)
print(mylist)

from random import randint 
print(randint(0,100))

