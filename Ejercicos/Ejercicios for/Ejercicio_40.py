#40. Crea un programa que cuente todos los números pares hasta el número 50
par=0
imp=0
for cont in range(50):
    if cont%2:
        par=par+1
    else:
        imp=imp+1
print("El total de numeros pares es:",par)
print("El total de numeros impares es:",imp)