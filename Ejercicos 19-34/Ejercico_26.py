#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

var=input("Introduce una letra: ")
var2=var.islower()

if var2==False:
 print("Esta letra esta en mayuscula.")
if var2==True:
 print("Esta letra es minúscula.")
    
