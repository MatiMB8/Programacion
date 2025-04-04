#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.

var=int(input("Introduce el numero de notas: "))
neg=0
neu=0
pos=0

for cont in range(var):
    var2=int(input("Introduce la nota: "))
    if var2<0:
        neg=neg+1
    elif var2>0:
        pos=pos+1
    else:
        neu=neu+1
print("la cantidad de numeros positivos es: ",pos)
print("La cantidad de numeros negativos es ",neg)
print("La cantida de ceros es: ",neu)

