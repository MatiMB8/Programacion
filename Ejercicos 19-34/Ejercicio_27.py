#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en
#caso de introducir un número, aparezca un aviso por pantalla

var=input("Introduce una letra: ")
var2=var.islower()

if var2==False:
    if var.isdigit()==True:
        print("El valor introducido es un número")
    else:
        print("Esta letra esta en mayuscula.")
if var2==True:
 print("Esta letra es minúscula.")
