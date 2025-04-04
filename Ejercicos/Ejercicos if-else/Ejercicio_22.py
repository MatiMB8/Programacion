#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

var=float(input("Introduce tu nota: "))

if var<0 or var>10:
    print("La nota que has introducido no esta entre el 0 y el 10.")
else:
    if var>=5:
        print("Has sacado un ",var," y has aprovado.")
    else:
        print("Has sacado un",var," y has suspendido")