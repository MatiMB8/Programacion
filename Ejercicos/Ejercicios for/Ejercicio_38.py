#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10

var=int(input("Cuantas notas quieres introducir? "))

for cont in range(var):
    var2=float(input("Introduce la nota: "))
    if 0>var2 or var2>10:
        print("Has introducido una nota equivocada")
    else:
        if var2<5:
            print("Asignatura suspendida")
        else: 
            print("Asignatura aprobada")