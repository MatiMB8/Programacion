#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

var1=float(input("Introduce la distancia de uno de los lados del trapecio: "))
var2=float(input("Ahora introduce su base menor: "))
var3=float(input("Ahora la base mayor: "))
var4=float(input("Finalmente, introduce la altura del trapecio: "))
print("El área del trapecio, según los datos introducidos, es: ",(var2+var3)/2*var4)
print("Y el perímetro del trapecio, segun los datos introducidos, es ",var2+var3+var1+var1)
