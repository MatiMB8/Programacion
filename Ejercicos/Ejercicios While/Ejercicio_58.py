import random
rep=3
var2=0
var=random.randint(1,5)
while rep!=0 and var!=var2:
    var2=int(input("Introduce un numero: "))
    if var2>5 or var2<1:
        print("Ese numero no se encuentra entre el 1 y el 5.")
    else:
        if var!=var2:
            print("Numero no acertado.")
        if var==var2:
            print("Numero acertado.")
    rep-=1