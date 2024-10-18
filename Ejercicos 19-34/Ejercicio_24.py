#24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente

var=float(input("Introduce el peso en kg: "))
var2=float(input("Introduce la altura en cm: "))
var_imc=round(var/(var2**2),2)
print(f"Si pesas {var} kilos y mides {var2}, tu IMC es:", var_imc)
if var_imc>25:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")


