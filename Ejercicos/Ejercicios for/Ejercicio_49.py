#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.

var=input("Introduce la palabra secreta: ")
lon=len(var)
var2=input("Introduce una letra: ")
var3=0
for cont in var:
    if cont == var2:
        print(f"La letra {var2} esta en la posicion {var3+1}")
    var3+=1