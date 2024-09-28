#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?


var=float(input("Introduzca un valor numerico: "))
var2=float(input("introduzca otro valor numerico: "))
print("la suma de ",var," y ",var2," es ",var+var2)
print("la resta de ",var," y ",var2," es ",var-var2)
print("la multiplicación de ",var," y ",var2," es ",var*var2)
print("la división de ",var," y ",var2," es ",round(var/var2, 2))
print("El exponente de ",var," y ",var2," es ",var**var2)
print("La división entera de ",var," y ",var2," es ",round(var//var2, 2))
