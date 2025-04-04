import random
siv=True
pts=100
tot=0
iat=0
iac=0
cts=[1,2,3,4,5,6,7,10,11,12]
print("Bienvenido al juego del 7 y medio")
var=input("¿Quieres carta? s/n: ")
while var!="n" and siv==True:
    car=random.choice(cts)
    if siv==True:
        iac=random.choice(cts)
    print("Tu carta es: ",car)
    if car==10 or car==11 or car==12:
        car=0.5
    if iac==10 or iac==11 or iac==12:
        iac=0.5
    iat=iac+iat
    tot=tot+car
    print("Acumulas: ",tot)
    if 7.5<=iat>=6.5:
        print("La bance se ha plantado")
        siv=False
    else:
        print("La banca roba otra carta")
    if tot>=7.5 or pts<=0:
        var="n"
    else:
        var=input("¿Quieres continuar? s/n: ")
    #if var=="n":
        #if tot==7.5:
            #print("¡Enhorabuena, has ganado la partida!")
            #pts=pts+10
        #elif tot>7.5:
           # print("Has superado los 7 y medio, has perdido!")
           # pts=pts-10
       # elif 6<=tot and 7>=tot:
           # print("Has sido un poco conservador, ¿no?")
          #  pts=pts+5
      #  elif tot<6:
       #     print("Quizas podrias haber arriesgado un poco mas...")
        #    pts=pts-5
      #  print(f"Tienes {pts} puntos")
       # if pts<=0:
          #  print("No te quedan puntos!")
       # else:
        #    var=input("Quieres jugar de nuevo? s/n: ")
          #  if var!="n":
            #    tot=0

                