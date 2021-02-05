#vardnicas jeb dictionaries
tel={"direktors":"67947253", "vietnieks":"65674720", "sekretare":"65826974"}
print(tel["sekretare"]) #noradot atslegu, izdruka vertibu

cenas={'piens':1.12, 'āboli':0.95, 'apelsīni':1.89}
print(cenas['piens'])
print(cenas['āboli'])
print(cenas['apelsīni'])

d={"k1":123, "k2":[10, 11, 12], "k3":{"atsl1":100, "atsl2":200}}
print(d["k3"]["atsl2"]) #izdruka iekšejas vardnicas vertibu
print(d["k2"][2]) #izdruka saraksta elementu

my_dict={'key1':['a', 'b', 'c']}
print(my_dict)
my_list=my_dict['key1']
print(my_list)
burts=my_list[2]
print(burts)
print(burts.upper()) #izdruka lielo C, kas atrodas vardnicas vertibā
print(my_dict['key1'][2].upper()) #viena rinda arlasa elementu un parveido

#pievienot jaunus objektus
new_dict={"k1":100, "k2":200}
print(new_dict)
new_dict["k3"]=300
print(new_dict)
new_dict["k1"]="simts"
print(new_dict)

#var piešķirt esošai atslegai jaunu vērtibu
new_dict["k1"]="simts"
print(new_dict)

#vardnicu metodes
print(new_dict.keys()) #izdruka visas atslegas
print(new_dict.values()) #izdruka vērtibas
print(new_dict.items()) #izdruka pārus
vertibu_list=list(new_dict.values())
print(vertibu_list)

#get
print(new_dict.get("k2"))
print(new_dict)
#pop
print(new_dict.pop("k2"))
print(new_dict)

new_dict.clear()
print(new_dict)