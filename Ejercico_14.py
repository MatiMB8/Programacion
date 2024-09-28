#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal.

import math

var=float(input("Introduce el diametro de tu circulo: "))
print("El area del circulo es ",round(math.pi*(var/2)**2,1))
print("y el perimetro del circulo es ",round(var*math.pi,1))
