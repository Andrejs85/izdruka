n = int(input("Ievadi naturalu skaitli: "))
while True:
    if n < 1:
        n = int(input("Ievadi naturalu skatli: "))
    else:
        break
nulles=0
for i in range(n):
    skaitlis=int(input(f"Ievadi {i+1}. no {n} veselajiem skaitļiem: "))
    if skaitlis==0:
        nulles+=1
print(f"Starp ievadītajiem {n} skaitļiem ir {nulles} nulles.")