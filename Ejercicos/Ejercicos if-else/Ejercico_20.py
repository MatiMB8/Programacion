#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10

var=int(input("Introduce un valor numerico entero menor de 11: "))
var2=int(input("Introduce otro valor numerico entero menor de 11: "))

if var>11 or var2>11:
    print("Uno de los numeros esta fuera de los limites establecidos")
else:
 if var<var2:
    print("El numero ", var2," es mayor que el numero ",var)
 if var>var2:
    print("El numero ", var, " es mayor que el numero ",var2)
 if var==var2:
    print("Ambos numeros son iguales.")
