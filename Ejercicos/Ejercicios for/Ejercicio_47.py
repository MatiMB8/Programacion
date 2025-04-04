#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida

var=int(input("Introduce el primer numero del primer intervalo: "))
var2=int(input("Introduce el segundo numero del primer intervalo: "))
var3=int(input("Introduce el primer numero del segundo intervalo: "))
var4=int(input("Introduce el segundo numero del segundo intervalo: "))
ae=""
oe=""
guion="-"
if var<var2:
    for cont in range(var,var2+1):
        ae=ae+"-"+str(var)
        if var != var2:
            var+=1
else:
    for cont in range(var2,var+1):
        ae=ae+"-"+str(var)
        if var2 != var:
            var-=1
ae=ae.lstrip(guion)
print(ae)

if var3>var4:
    for cont in range(var3,var4+1):
        oe=oe+"-"+str(var3)
        if var3 != var4:
            var3+=1
else:
    for cont in range(var4,var3+1):
        oe=oe+"-"+str(var4)
        if var4 != var3:
            var3-=1
    
oe=oe.lstrip(guion)
print(oe)