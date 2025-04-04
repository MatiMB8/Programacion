import random

sn=""
pts=[]
var3=8
lis=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
var=random.choice(lis)

var2=input("Introduce la palabra secreta: ")
while sn!="n":
    if var2!=var:
        var2=input("Incorrecto. Sigue probando: ")
        if var3>=1:
            var3-=1
    else:
        print("Has acertado!")
        sn=input("Deseas continuar?: ")
        pts.append(var3)
sma=sum(pts)
print("Puntuacion ",pts)
print("Tu puntuación ha sido de ",sma)
print("La media de las partidas realizadas es ", sma/len(pts))
if sma>=sma/len(pts):
    print("Tienes buena suerte...")
else:
    print("Dedicate al parchís")

