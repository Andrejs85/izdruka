def saskaiti_skaitlus(sk1, sk2):
    #rez=sk1+sk2
    return sk1+sk2
    
rez1=saskaiti_skaitlus(2,3)
rez2=saskaiti_skaitlus(2.3, 35.8)
rez3=saskaiti_skaitlus(2.5, 13)
print(rez1+rez2+rez3)

#parbauda vai ir pāra skaitlis
def parbaudi_pari(skaitlis):
    return skaitlis%2==0

print(parbaudi_pari(20))
print(parbaudi_pari(15))
print(parbaudi_pari(4))

#atgriezis true, ja sarakstā atrodas kaut viens pāra skaitlis
def parbaudi_pari_list(saraksts):
    for skaitlis in saraksts:
        if skaitlis%2==0:
            return True # pec return funkcijas darbiba apstajas
        else:
            pass
    return False

print(parbaudi_pari_list([1,5,3,7]))

"""
#atgriež visus pāra skaitļus, kas ir sarakstā
def parbaudi_pari_list2(saraksts):
    para_skaitli=[]
    for skaitlus in saraksts:
        if skaitlis%2==0:
            para_skaitli.append(skaitlis)
        else:
            pass
    return para_skaitli

print(parbaudi_pari_list2([1,2,3,4]))
"""