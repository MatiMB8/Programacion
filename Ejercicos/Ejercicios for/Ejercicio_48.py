#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra.

var=input("Introduce la palabra secreta: ")
lon=len(var)

for cont in range(lon):
    print("Introduce una letra: ")
    if var1 in var:
        print("La letra existe")
    else:
        print("La letra no existe")
    
    