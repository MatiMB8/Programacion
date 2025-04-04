var3=""
while var3!="n":
    var=int(input("Intoduce un numero entero: "))
    var2=int(input("Introduce otro: "))
    print(f"La suma de esos dos numeros da {var+var2}")
    var3=input("Quieres repetir la operacion? s/n: ")
else:
    print("Programa finalizado.")