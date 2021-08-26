#piemers=[1,2,3,4,5,6,7]
from random import shuffle 

#shuffle(piemers) #shuffle funkcija neatgriež rezultātu
#print(piemers)

#izveido shuffle funkciju, kas atgriež rezultātu
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
#rezult=shuffle_list([1,2,3,4,5])
#print(rezult)

#izveido 3 "glazītes", kur vienā ir bumbiņa 
#myList=[" ","o"," "]
#print(shuffle_list(mylist))

#izveido funkciju, kas minēs 
def mans_minejums():
    minejums=""
    while minejums not in ["0", "1", "2"]:
        minejums=input("Izvelies skaitli - 0, 1, 2: ")
    return int(minejums)
#indekss=mans_minejums()

#izveido funkciju, kas parbauda vai minejums sakrit
def parbaudi_minejumu(mylist, minejums):
    if mylist[minejums-1]=="o":
        print("Uzvarēji!") #windows +.
    else:
        print("Zaudēji...")
        print(mylist)
#parbaudi_minejumu(mylist, indekss)

#pa soļiem izsauc visas funkcijas 
# norada sarakstu
mylist=[" ", "o", " "]

#sajauc sarakstu
sajaukts_saraksts=shuffle_list(mylist)

#speletaja minejums
spelet_minejums=mans_minejums()

#parbauda speletaja minejumu
parbaudi_minejumu(sajaukts_saraksts,spelet_minejums)