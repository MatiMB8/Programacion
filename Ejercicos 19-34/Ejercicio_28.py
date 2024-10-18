#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza
#elif.

var=input("Introduce una letra: ")
var2=var.islower()
var3=var.isalpha()

if var.isdigit()==True:
    print("El valor introducido es un número")
elif var3==True and var2==False:
    print("Esta letra esta en mayuscula.")
elif var3==True and var2==True:
    print("Esta letra es minúscula.")
else:
    print("El valor introducido es un simbolo")
    

