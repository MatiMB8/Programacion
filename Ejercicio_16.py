#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).

import math

var=float(input("Introduce un valor numerico entero: "))
var2=math.sqrt(var)
print("El resultado de la raiz es: ",round(var2,1))
print("El resultado de la división es ",var2//2)
