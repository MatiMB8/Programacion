#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda.
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

var="A quién madruga Dios ayuda"
print(var)
var2=input("Preguntame alguna palabra y te diré si esta en mi frase: ")
var3=var.find(var2)
if var3>-1:
    print("La palabra esta en la frase y esat en el indice ",var3)
if var.find(var2)==-1:
    print("La palabra no esta en la frase.")


