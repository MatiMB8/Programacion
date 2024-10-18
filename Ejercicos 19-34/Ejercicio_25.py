#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos

var=float(input("Introduce tu nota: "))

if var<0 or var>10:
    print("La nota que has introducido no esta entre el 0 y el 10.")
else:
    if var<5:
        print("Has sacado un ",var,", tu nota es insuficiente.")
    if var>=5 and var<6.5:
       print("Has sacado un",var,", tu nota es satisfactoria.")
    if var>=6.5 and var<8.5:
        print("Has sacado un ",var,", tu nota es notable.")
    if var>=8.5 and var<=10:
        print("Has sacado un ",var,", tu nota es excelente.")

        

