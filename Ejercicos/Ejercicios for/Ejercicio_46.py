#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.
    
voc=""
con=""
var=input("Intorduce una palabra: ")
var2=var.lower()
lon=len(var)
for cont in range(0,lon):
    if var[cont] not in "AÁEÉIÍOÓUÚaáeéiíoóuú":
        con=con+var[cont]
    else:
        voc=voc+var[cont]
print(f"Las vocales de la palabra {var} son: {voc}")
print(f"Las consonantes de la palabra {var} son: {con}")
