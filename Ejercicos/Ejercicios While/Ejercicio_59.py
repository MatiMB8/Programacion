import random
cont=0
var=random.randint(0,1000)
var2=int(input("Introdice un numero entero entre el 0 y el 1000: "))

while var2!=var:
    if var2<var:
        print("El numero que has introducido es menor que el mio")
        cont+=1
    elif var2>var:
        print("El numero que has introducido es mayor que el mio")
        cont+=1
    var2=int(input("Introdice un numero entero entre el 0 y el 1000: "))
else:
    print(f"Has acertado. Has necesitado {cont} intentos")
