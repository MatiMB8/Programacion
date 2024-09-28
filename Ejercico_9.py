#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos 
#y las horas

var=float(input("Introduce un numero de segundos: "))
print("Ese valor son ",var/60," en minutos y ",round(var/3600,2)," en horas.")
