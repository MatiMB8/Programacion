#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
    
vocales=["a","á","e","é","i","í","o","ó","u","ú"] 
voc=""
con=""
var=input("Intorduce una letra: ")
lon=len(var)
for cont in range(0,lon):
    if var[cont] not in vocales:
        con=con+var[cont]
    else:
        voc=voc+var[cont]
print(f"Las vocales de la palabra {var} son: {voc}")
print(f"Las consonantes de la palabra {var} son: {con}")
        