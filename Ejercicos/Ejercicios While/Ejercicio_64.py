par=0
imp=0
pos=0
neg=0
zer=0
res=0
var=int(input("Introduce un numero: "))
while var!=-99:
    if var%2==0:
        par+=1
    if var%2!=0:
        imp+=1
    if var>0:
        pos+=1
    if var<0:
        neg+=1
    if var==0:
        zer+=1
    res=res+var
    var=int(input("Introduce un numero: "))
else:
    print("RESUMEN")
    print("El numero de pares es: ",par)
    print("El numero de impares es: ",imp)
    print("El numero de numeros positivos es: ",pos)
    print("El numero de numeros negativos es:",neg)
    print("El numero de zeros introducidos es: ",zer)
    print("La suma de todos los numeros introducidos es: ",res)