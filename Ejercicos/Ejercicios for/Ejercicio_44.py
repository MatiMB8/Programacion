#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’

res="0"
var=0
for cont in range(3,100,3):
    res=res+","+str(cont)

print(res)
    
    

