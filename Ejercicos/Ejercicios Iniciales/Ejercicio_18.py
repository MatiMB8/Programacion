#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.

var=int(input("Cuantos menores de 18 años entraran al cine? "))
var2=int(input("Y cuantos adultos entrarán al cine? "))
print("La entrada de ",var," menor/es costaria un total de ",round(12*0.5*var,2),"€")
print("Y la entrada de ",var2," adultos costaria un total de ",round(12*0.1*var2,2),"€")
