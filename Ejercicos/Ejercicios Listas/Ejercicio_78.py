sn=""
lis=["a","b","D","x","r","X","3","h","w","2","i"]
while sn!="n":
    var=input("Que valor numerico deseas suprimir de la lista?: ")
    if var.isnumeric():
        if var in lis:
            lis.remove(var)
            print(lis)
        else:
            print("El numero no se encuentra en la lista")
    else:
       print("Introduce valor numerico.")
    sn=input("Deseas continuar? s/n ")
