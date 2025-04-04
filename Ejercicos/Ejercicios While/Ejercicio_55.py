
cont=0
resf=0

while resf<50 and resf%2!=0:
    cont+=1
    var=int(input("Intoduce un numero entero: "))
    var2=int(input("Introduce otro: "))
    res=var+var2
    print("El resultado de la suma es: ", res)
    resf=resf+res
    if cont==1:
        print(f"el total acumulado es {resf} y llevas {cont} operacion realizada")
    else:
        print(f"el total acumulado es {resf} y llevas {cont} operaciones realizadas")
        
    
    
