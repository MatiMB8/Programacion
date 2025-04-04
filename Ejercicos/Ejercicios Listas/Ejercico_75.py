lis=["a","b","D","x","r","X","3","h","w","2","i"]
upp=0
let=0
num=0
sma=0
tot=0
for cont in lis:
    if cont.isalpha():
        let+=1
        if cont.isupper():
            upp+=1
    elif cont.isnumeric():
        num+=1
        sma=sma+int(cont)
    tot+=1
print(f"Numero de valores: {tot}")
print(f"Cantidad de numeros: {num}")
print(f"Cantidad de letras: {let}")
print(f"Cantidad de mayusculas: {upp}")
print(f"Suma total de numeros: {sma}")