#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

var=float(input("Introduce tu peso en kilogramos: "))
var2=float(input("Ahora itroduce tu estatura en metros: "))
var3=round(var/var2**2,2)

if var3<=25:
    print("Si pesas ",var," kilos y mides ",var2,", tu IMC es: ",var3)
else:
    print("Si pesas ",var," kilos y mides ",var2,", tu IMC es: ",var3,". Hay sobrepeso.")
    
