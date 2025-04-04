lis1=["casa","mesa","sal","sol","agua"]
lis2=["casa","luz","tres","tren","sol","pan"]
rep=[]
nor=[]

for cont in range(len(lis1)):
    if lis1[cont] in lis2:
        rep.append(lis1[cont])
    else:
        nor.append(lis1[cont])
print(f"Estan repetidas: {rep}")
print(f"No estan repetidas: {nor}")