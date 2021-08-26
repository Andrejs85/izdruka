#args (arguments) - atgriež tuple
def myfunc(a,b,c):
#atgriež 5% no a un b summas
    return sum((a,b,c))*0.05

print(myfunc(60,40,100))

#args

def myfunc2(*args):
    return sum(args)*0.05 # ļauj padot tik argumentus, cik nepieciešams

print(myfunc2(60,40,100,5,20))

#kwargs (key word arguments) - atgriž vardnicu

def myfuncKw(**kwargs):
    if "auglis" in kwargs:
        print(f"Mana izvele ir {kwargs['auglis']} un {kwargs['darzenis']}.")
    else:
        print("Nevienu augli neatrodu.")

myfuncKw(auglis="ābols", darzenis="burkāns")

