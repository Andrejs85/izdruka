# if, else, elif
"""
if nosacijums:
    izpildāmās darbības
 elif cits nosacījums:
    izpildāmās darbības
else:
    izpildāmās darbības visos citos gadijumos
"""
#ja skaitlis  ir lielāks par 5, tad izdrukā, ka lielāks par 5, citādi, ja skaitlis lielāks par 0, izdrukā, ka lielāks par 0.Citādi izdrukā, ka tas nav pozitivs skaitlis

a = -1
if a > 5:
    print("Šis skaitlis ir lielāks par 5.")
elif a > 0:
    print(f"Skaitlis {a} ir lielāks par 0.")
else:
    print(f"Skaitlis {a} nav pozitivs.")

if True:
    print("Patiesi")

suns_grib_est = False

if suns_grib_est:
    print("Pabaro suni!")
else:
    print("Suns ir paēdis.")
