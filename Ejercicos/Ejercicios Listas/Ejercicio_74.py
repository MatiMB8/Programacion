lis1=["casa","mesa","sal","sol","agua"]
lis2=["casa","luz","tres","tren","sol","pan"]
rep=[]
nor=[]

for cont in range(len(lis2)):
    if lis2[cont] in lis1:
        rep.append(lis2[cont])
    else:
        nor.append(lis2[cont])
for cont in range(len(lis1)):
    if lis1[cont] in lis2:
        rep.append(lis1[cont])
    else:
        nor.append(lis1[cont])
        
print(f"Estan repetidas: {set(rep)}")
print(f"No estan repetidas: {set(nor)}")