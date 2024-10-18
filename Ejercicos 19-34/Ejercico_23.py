#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.


var=float(input("Introduce tu nota: "))


if var<5:
        print("Has sacado un ",var,", tu nota es insuficiente.")
elif var>=5 and var<6.5:
       print("Has sacado un",var,", tu nota es satisfactoria.")
elif var>=6.5 and var<8.5:
        print("Has sacado un ",var,", tu nota es notable.")
elif var>=8.5 and var<=10.:
        print("Has sacado un ",var,", tu nota es excelente.")
else:
    print("La nota que has introducido no esta entre el 0 y el 10.")
        