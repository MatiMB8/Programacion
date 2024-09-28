#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: 
#cociente, resto y si el dividendo es par o impar.

var=float(input("Introduce un valor numérico: "))
var2=float(input("Introduce otro valor numérico: "))
print("El cociente es: ",var/var2)
print("El resto es: ",var%var2)
if var %2 == 0:
    print("El número es par")
else:
    print("el número es impar")
