#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.

var=int(input("Cuantas notas quieres introducir? "))

for cont in range(var):
    var2=float(input("Introduce la nota: "))
    if var2<5:
        print("Asignatura suspendida")
    else:
        print("Asignatura aprobada")