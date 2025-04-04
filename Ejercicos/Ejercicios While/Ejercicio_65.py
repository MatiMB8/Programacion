may=0
men=0
var=0
while var!=-99:
    num=var
    var=int(input("Introduce un numero: "))
    if var>num:
        may=var
    if var==-99:
        num=num
    elif var<num:
        men=var
    
    
else:
    print("RESUMEN")
    print("El numero mas grande es: ",may)
    print("El numero mas pequeño es: ",men)
   