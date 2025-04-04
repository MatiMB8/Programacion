import random

lis=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
var=random.choice(lis)

var2=input("Introduce la palabra secreta: ")

while var2!=var:
    var2=input("Incorrecto. Sigue probando: ")
else:
    print("Has acertado!")

