#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif

var2=input("Introduce una frase: ")
var=len(var2)
if var<11:
    print("La frase tiene menos de 11 caracteres.")
elif var>11:
    print("La frase tiene más de 11 caracteres.")
else:
    print("La frase tiene 11 caracteres.")
