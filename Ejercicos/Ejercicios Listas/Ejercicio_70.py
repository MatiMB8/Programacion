lst=[]
lis=[]
num=1
var=int(input("Introduce la cantidad de palabras: "))
for cont in range(var):
    var2=input(f"Introudce la {num}ª palabra: ")
    lis.append(var2)
    lst.append(var2)
    num+=1
    lis.sort()
print(lis)
lst.reverse()
print(lst)
   