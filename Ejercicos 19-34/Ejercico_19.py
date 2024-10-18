#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
#iguales

var=int(input("Introduce un valor numerico entero: "))
var2=int(input("Introduce otro valor numerico entero: "))


if var<var2:
    print("El numero ", var2," es mayor que el numero ",var)
elif var>var2:
    print("El numero ", var, " es mayor que el numero ",var2)
else:
    print("Ambos numeros son iguales.")
