lis=["a","b","D","x","r","X","h","w","i"]
num=["2","3"]

var=int(input("Introduce 1 para visualizar el orden ascendente o 2 para el descendente: "))

if var==1:
    print(num)
    print(lis)
elif var==2:
    lis.reverse()
    num.reverse()
    print(num)
    print(lis)
else:
    print("numero no valido")

