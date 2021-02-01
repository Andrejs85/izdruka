#lists jeb saraksti
#['Sveika,', 100,'tu' ,3.59,'skaista!', [1,26]]
myList=[1,2,3, 100,'tu' ,3.59,'skaista!']
print(len(myList)) #saraksta garums

my_list=["viens", "divi", "tris", "četri"]
print(my_list[0]) #izdruka elementu ar noradīto indeksu
print(my_list[1:3]) #izdrukā no noradīta indeksa līdz beigām

#sarakstu apvienošana jeb konkatinācija
cits_list=["pieci", "seši"]
print(my_list+cits_list) #izdrukā sarakstu ar abu mainīgo elementiem
jauns_list=my_list+cits_list
print(jauns_list)

#sarakstu mainīšana
jauns_list[0]=1
print(jauns_list)

jauns_list.append("septiņi") #pievieno pēdejo elementu
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

pop_elem=jauns_list.pop(0) #noņem pēdejo elementu
print(jauns_list)
print(pop_elem)

#elementu kartošana
new_list=['b', 'a', 'z', 'e']
print(new_list)
num_list=[4,1,8,3]
print(num_list)
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
myList=[1,2,3, 100,3.59,]
myList.sort()
print(myList)

#saraksts saraksta (nested)
nested_list=[1,5,[7,2]]
print(nested_list[2][1])

augli=["ābols", "banāns", "gurķis"]
print(augli[2])

#aizstajam elementu - gurķis ->apelsīns
augli[2]="apelsīns"
print(augli)

#pievienot beigas "bumbieris"
augli.append("bumbieris")
print(augli)

#iespraust konkrēta vieta jaunu elementu "citrons"
#insert
augli.insert(2,"citrons")
print(augli)

#izņemt no saraksta "banāns"
augli.pop(1)
print(augli)

#izdrukat pilna teikuma, cik ir sarakstā
print(f"Sarakstā ir {len(augli)} dažadi augļi.")
