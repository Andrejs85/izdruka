
vards=input("Kā tevi sauc? ")
print("Labdien, " +vards)

vecums=int(input("Cik tev gadu? "))
#print("Tev ir " +vecums+ " gadi.")
print(f"Tev ir {vecums} gadi.")
print(f"Tavs dzimšanas gads ir {2021-vecums}.")
dzimsGads=2021-vecums
print(f"Tavs dzimšanas gads ir {dzimsGads}.")
temperatura=float(input("Ievadi temperatūru pēc Celsija: "))
print(f"Temperatura pēc Farenheita skalas ir {temperatura*9/5+32} grādi.")
#Uzraksti programu, kura
platums=float(input("Ievadi telpas platumu: "))
garums=float(input("Ievadi telpas garumu: "))
augstums=float(input("Ievadi telpas augstumu: "))
print(f"Telpas tilpums ir {platums*garums*augstums}.")


#Strings (rakstzīmju virknes)
print("sveiki")
print('sveiki')
print("I'm going on a run")
print('Arī šis ir risinājums"')
print("Sveika, \npasaule!")
print("Sveika, \tpasaule!") #drukā ar tabulācijas atkāpi

#String garums-len()
print(len("sveiki"))
print(len("Ko tu domā?"))


# [sākums:beigas:solis]
myString="Sveiki, pasaule"
print(myString)
print(myString[0] ) #izdrukā pirmo rakstzīmi (ar indeksu 0)
print(myString[8] ) #izdrukā rakstzīmi ar 8. indeksu
print(myString[-1] ) #izdrukā pedējo simbolu
print(myString[13] ) #izdrukā 14. rekstzīmi
print(myString[-3] ) #izdrukā 14. rekstzīmi
myString="abcdefghijklmnoprstuvz"
print(myString)
print(myString[2] ) #izdrukā c
print(myString[2:] ) #izdrukā visu, sākot no c
print(myString[:3] ) #izdrukā visu līdz 3.indeksam(neieskaitot)
print(myString[3:6] ) #izdrukā visu no 3 līdz 5 indeksam
print(myString[::] ) #izdrukā visu
print(myString[::2] ) #izdrukā katru otro rakstzīmi
print(myString[::3] ) #izdrukā katru trešo rakstzīmi
print(myString[2:7:2] ) #izdrukā katru otro  rakstzīmi no 2. līdz 6. indeksam 
print(myString[::-1] ) #izdrukā visu no otra gala