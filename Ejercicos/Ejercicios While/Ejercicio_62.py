var=int(input("Introduce un numero entero: "))
var2=int(input("Introduce otro: "))
cont=var
par=""
imp=""

while cont!=var2:
    if cont%2==0:
        par=par+"-"+str(cont)
    if cont%2!=0:
        imp=imp+"-"+str(cont)
    if var>var2:
        cont-=1
    if var<var2:
        cont+=1
    
else:
    par=par.lstrip("-")
    imp=imp.lstrip("-")
    print(f"Los numeros pares son {par}")
    print(f"Los numeros impares son {imp}")        
        
    