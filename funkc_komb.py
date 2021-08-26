#Izveido suluspiedi, kas izspiež sulu no aboliem un apelsiniem
#izveido funkciju, kas "sagriež" augli 4 gabalos 
def griezejs(augli):
    return augli*4

abolu_gab=griezejs(9)
apelsinu_gab=griezejs(6)
print(abolu_gab)
print(apelsinu_gab)

#izveido funkciju, kas paziņo no cik gabaliem izspiesta sula 
def suluspiede(abolu_gab, apelsinu_gab):
    print(f"Sula no {abolu_gab} abolu gabaliem un {apelsinu_gab} apelsinu gabaliem.")

suluspiede(abolu_gab,apelsinu_gab)

#otrais variants - funkcija funkcijā
def griezejs2(augli):
    return augli*4

def suluspiede2(aboli, apelsini):
    abolu_gab=griezejs2(aboli)
    apelsinu_gab=griezejs2(apelsini)
    print(f"Sula no {abolu_gab} abolu gabaliem un {apelsinu_gab} apelsinu gabaliem.")
suluspiede2(45,16)