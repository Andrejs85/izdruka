#3. grupa
#1. Izveido funkciju, kas pārbauda divus veselos skaitļus. Ja kāds no tiem vai to summa ir 10, funkcija atgriež True.

def parbaude(a,b):
    if a==10 or b==10 or a+b==10:
        True
    else:
        return False

print(parbaude(5,4))

#2. Dots string. Izveido funkciju, kas atgriež šo string un pieraksta tam priekšā “not”. Ja string jau sākas ar “not”, tad atgriež pašu ievadīto string. Paraugs: vilciens -> notvilciens, notārs -> notārs

#vilciens -> notvilciens, notārs -> notārs
x=input("Ievadi vardu: ")
x[0:]
y=x[0:]
print(y, "->", "not" + y)

