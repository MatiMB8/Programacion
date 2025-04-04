boc=0
pat=0
beb=0
var4=""
cont=0
res=0
desc=0
print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5 €")
print("2. Patatas gruesas - 1.75 €")
print("3. Patatas rústicas - 2 €")
print("BEBIDAS")
print("1. Coca cola - 2 €")
print("2. Acuarius - 1.5 €")
print("3. Agua - 1 €")

while var4!="n":
    cont+=1
    var=int(input("Escoja un tipo de bocadillo: "))
    var2=int(input("Escoja un acompañamiento para su bocadillo: "))
    var3=int(input("Escoja una bebida: "))
    if var==1:
        boc=9
    if var==2:
        boc=4.5
    if var==3:
        boc=2.5
    if var2==1:
        pat=1.5
    if var2==2:
        pat=1.75
    if var2==3:
        pat=2
    if var3==1:
        beb=2
    if var3==2:
        beb=1.5
    if var3==3:
        beb=1
    if var>3 or var2>3 or var>3:
        print("ERROR. Has introducido un numero no valido.")
        var4="s"
    var4=input("Quiere ordenar otro menu? s/n: ")
    res=res+boc+beb+pat
    iva=res+(res*10)/100
    if 30<iva>=20:
        desc=iva-(iva*5)/100
    if iva>=30:
        desc=iva-(iva*15)/100
    desc=round(desc,2)
else:
    print(f"Has realizado {cont} pedidio/s.")
    print (f"El precio a pagar es: {res}")
    print(f"El precio con IVA incluido es: {iva}")
    if desc>0.1:
        print(f"El precio con descuento es: {desc}")    
    




