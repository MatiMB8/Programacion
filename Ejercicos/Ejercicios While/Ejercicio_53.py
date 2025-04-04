cont=0
resf=0
var3=""
while var3!="n":
    cont+=1
    var=int(input("Intoduce un numero entero: "))
    var2=int(input("Introduce otro: "))
    res=var+var2
    resf=resf+res
    print(f"La suma de esos dos numeros da {res}")
    var3=input("Quieres repetir la operacion? s/n: ")
else:
    print(f"La suma total es {resf} y el numero de repeticiones es {cont} ")

        
        
