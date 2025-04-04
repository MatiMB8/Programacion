#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para
#no distinguir entre mayúsculas y minúsculas



var="A quién madruga Dios ayuda"
var1=var.lower()

print(var)
var2=input("Preguntame alguna palabra y te diré si esta en mi frase: ")
var4=var2.lower()
var3=var1.find(var4)
if var3>-1:
    print("La palabra esta en la frase y esta en el indice ",var3)
if var1.find(var4)==-1:
    print("La palabra no esta en la frase.")
    

