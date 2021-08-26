print("  Krustini/nullites  ")
laukums= list(range(1,10))
def zimet_laukumu(laukums):
    print("_____________")
    for i in range(3):
        print("|", laukums[0+i*3], "|", laukums[1+i*3], "|", laukums[2+i*3], "|")
        print("_____________")

zimet_laukumu(laukums)

while True:
    x=int(input("  Speletajs_1: kur likt X ?  "))
    if x==1:
        laukums[0]="x"
    if x==2:
        laukums[1]="x"
    if x==3:
        laukums[2]="x"
    if x==4:
        laukums[3]="x"
    if x==5:
        laukums[4]="x"
    if x==6:
        laukums[5]="x"
    if x==7:
        laukums[6]="x"
    if x==8:
        laukums[7]="x"
    if x==9:
        laukums[8]="x"
    uzvara_x=(laukums[0]==laukums[1]==laukums[2]=="x") or (laukums[3]==laukums[4]==laukums[5]=="x") or (laukums[6]==laukums[7]==laukums[8]=="x") or (laukums[0]==laukums[3]==laukums[6]=="x") or (laukums[1]==laukums[4]==laukums[7]=="x") or (laukums[2]==laukums[5]==laukums[8]=="x") or (laukums[0]==laukums[4]==laukums[8]=="x") or (laukums[2]==laukums[4]==laukums[6]=="x")
    zimet_laukumu(laukums)
    if uzvara_x==True:
        print("  Speletajs_1 uzvareja.  ")
        break

    o=int(input("  Speletajs_2: kur likt O ?  "))
    if o==1:
        laukums[0]="o"
    if o==2:
        laukums[1]="o"
    if o==3:
        laukums[2]="o"
    if o==4:
        laukums[3]="o"
    if o==5:
        laukums[4]="o"
    if o==6:
        laukums[5]="o"
    if o==7:
        laukums[6]="o"
    if o==8:
        laukums[7]="o"
    if o==9:
        laukums[8]="o"
    uzvara_o=(laukums[0]==laukums[1]==laukums[2]=="o") or (laukums[3]==laukums[4]==laukums[5]=="o") or (laukums[6]==laukums[7]==laukums[8]=="o") or (laukums[0]==laukums[3]==laukums[6]=="o") or (laukums[1]==laukums[4]==laukums[7]=="o") or (laukums[2]==laukums[5]==laukums[8]=="o") or (laukums[0]==laukums[4]==laukums[8]=="o") or (laukums[2]==laukums[4]==laukums[6]=="o")
    zimet_laukumu(laukums)
    if uzvara_o==True:
        print("  Speletajs_2 uzvareja.  ")
        break
    