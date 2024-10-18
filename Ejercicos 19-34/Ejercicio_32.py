#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para
#no distinguir entre mayúsculas y minúsculas

var="A quién madruga Dios ayuda"

print(var)
var2=input("Preguntame alguna palabra y te diré si esta en mi frase: ")
var3=var.find(var2)
if var3>-1:
    print("La palabra esta en la frase y esta en el indice ",var3)
if var.find(var2)==-1:
    print("La palabra no esta en la frase.")

