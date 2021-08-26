"""
#1
mystring = "hello"
my_list = [burts for burts in mystring]
print(my_list)
my_list = [x for x in "tekstiņš"]
print(my_list)

#2

mylist = [x for x in range(0, 11)]
print(mylist)
mylist = [x**2 for x in range(0, 11)]
print(mylist)

#3

mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)

#4

celsiji = [0, 10, 20, 34.5]
farenheiti = [(9 / 5) * temp + 32 for temp in celsiji]
print(farenheiti)

#5
#nested lists

mylist=[]
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)
mylist2 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist2)


def order_food(dish):
    print(f"I am ordering {dish}")
    print(f"{dish.capitalize()} should be pretty tasty")

# go to restaurant
def eat():
    # everything after indent will be run by this function
    print("Hello")
    #print("Let's order some food")
    order_food("potatoes")
    order_food("ice cream")
    print("Let's eat")
    print("Let's leave and be happy")
# call the function 2 times
#eat()
eat()
#eat()

# we can give our functions parametrs and those parametrs take arguments
"""


def funkcijas_nosaukums(arguments1, arguments2):
    
    #Funkcijas apraksts
    
    print("Sveiki", arguments1, arguments2) #visas darbibas, ko veic funkcija


funkcijas_nosaukums("Ieva", 12)
funkcijas_nosaukums("Agnese", 10)
funkcijas_nosaukums("Katrīna", 20)
#funkcijas_nosaukums("")


def pilseta(nosaukums, valsts):
    print(nosaukums, " ir pilsēta", valsts) 

pilseta("Salaspils", "Latvijā.")
pilseta("Rīga", "Latvijā")

