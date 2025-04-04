#43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra

var=input("Introduce una palabra: ")
lon=len(var)

for cont in range(0,lon):
    print("En la posicion ",cont, "esta la ",var[cont])
