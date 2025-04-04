#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

var=int(input("Introduce un numero natural: "))
var3=1
res=0
for cont in range(var):
   res=res+cont+1
print("La suma total de numeros naturales es", res)