#tuples - līdzigi list, bet nav maināmi (iekavas) , sakartots
my_tup=(1, 2, 3)
my_list=[1, 2 ,3]
print(type(my_tup))
print(type(my_list))
print(len(my_tup))

#var saturet dažadus datu tipus
my_tup=("es",6,6, 2.58 )
print(my_tup)

#var indekset
print(my_tup[0])
print(my_tup[-1])

#metodes
print(my_tup.count(6)) #saskaita cik reizes atkartojas konkretais objekts
print(my_tup.index(6)) #parada indeksu kur pirmo reizi paradas objekts

#nav maināms
my_list[0]="viens"
print(my_list)
#my_tup[0]="viens"
print(my_tup)

#sets - nesakartota unikalu objektu kopa
my_set=set()
print(my_set)
my_set.add(1)
print(my_set)
my_set.add(2)
print(my_set)
my_set.add(1.26)
print(my_set)
my_set.add(2)
print(my_set)
my_list=[1,1,1,11,2,2,22,2,3,333,3,3,3,3,3,3]
print(set(my_list))

#piemers
s="Salaspils"
my_set=set(s)
print(my_set)

#booleans - True vai False - izmanto bieži loģiskajos operatoros
print(True) #ar lielo burtu
print(type(False))

#piemers
print(1>2)
print(1==1)