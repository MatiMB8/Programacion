#41. Imprime el siguiente patron utilizando for:
var="54321"
lon=len(var)
for cont in range(0,lon):
    print(var)
    var=var[1:lon]
    
