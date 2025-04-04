import random
siv=True
ent=False
iae=False
tot=0
iat=0
iac=0
cts=[1,2,3,4,5,6,7,10,11,12]
ial=[6,6.5,7]
var=""
print("Bienvenido al juego del 7 y medio!")

usr=input("Cual es tu nombre?: ")
print(f"Ok {usr}, Comencemos!")
print(f"-------TURNO DE {usr.upper()}-------")
while var!="n" and siv==True:
    var=input("¿Quieres carta? Presiona n para cancelar: ")
    while var!="n":
        car=random.choice(cts)
        print("Tu carta es: ",car)
        if car==10 or car==11 or car==12:
            car=0.5
        tot=tot+car
        print(f"{usr} acumula {tot} puntos")
        if tot>7.5:
            print("Te has pasado! Te plantas automaticamente")
            ent=True
            var="n"
        elif tot==7.5:
            print("Puntuacion perfecta! Te plantas automaticamente")
            var="n"
        else:
            var=input("¿Quieres continuar? s/n: ")
        if var=="n":
            if 6<=tot and 7>=tot:
                print("Has sido un poco conservador, ¿no?")
            elif tot<6:
                print("Quizas podrias haber arriesgado un poco mas...")
    while siv==True:
        print("-------TURNO DE LA BANCA-------")
        iac=random.choice(cts)
        print(f"La carta de la banca es {iac}")
        if iac==10 or iac==11 or iac==12:
            iac=0.5
        iat=iac+iat
        input(f"La banca acumula {iat} puntos")
        if iat in ial:
            print("La banca se ha plantado")
            siv=False
        elif iat==7.5:
            print("La banca se ha plantado")
            siv=False
        elif iat>7.5:
            print("La banca se ha plantado")
            siv=False
            iae=True
        else:
            print("La banca roba carta...")
    if var=="n" and siv==False:
        print("----------------------------RESULTADOS-------------------------------------")
        print(f"Tu puntuacion ha sido de {tot} y la puntuacion de la banca ha sido de {iat}")
        if tot==7.5 and iat!=7.5:
            print("Has ganado con puntuacion perfecta!")
        elif iat==7.5 and tot!=7.5:
            print("La banca ha ganado con puntuacion perfecta!")
        elif ent==True and iae==True:
            print("Los dos os habeis pasado... No hay ganador!")
        elif iae==True and ent==False:
            print("La banca se ha pasado de 7.5... Has ganado!")
        elif iat>tot:
            print("La banca ha conseguido mas puntos que tu sin pasarse... Has perdido!")
        elif iae==False and ent==True:
            print("Has perdido por pasarte de 7.5!")
        elif tot>iat:
            print("Has conseguido mas puntos que la banca sin pasarte... Has ganado!")
        elif iat==tot:
            print("Habeis conseguido los mismos puntos... No hay ganador!")
        var=input("Quieres volver a jugar? Presiona n para cancelar ")
        if var!="n":
            print(f"-------TURNO DE {usr.upper()}-------")
            siv=True
            tot=0
            iat=0 
else:
    print("Vuelve cuando quieras!")