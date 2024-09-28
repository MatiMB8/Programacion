#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
#introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math

var=int(input("Introduce el radio del cilindro: "))
var2=int(input("Ahora introduce la altura del cilindro "))
print("El area del cilindro es",round(2*math.pi*var*(var+var2),2))
print("y el perimetro será ",round(math.pi*var**2*var2,2))
