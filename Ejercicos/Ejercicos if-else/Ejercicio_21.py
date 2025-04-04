#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo

import math
var=int(input("Introduce un valor numerico entero: "))
var2=int(input("Introduce otro: "))
var3=int(input("Introduce otro: "))

sqrt=(var2**2)-(4*var*var3)
if sqrt<0:
    print("La raiz no puede er un valor negativo")
else:
    x1=(-var2+math.sqrt(sqrt))/2*var
    x2=(-var2-math.sqrt(sqrt))/2*var
    print("El valor de x1 es",x1)
    print("El valor de x2 es ",x2)
    