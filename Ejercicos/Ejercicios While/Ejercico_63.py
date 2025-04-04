import random
uno=0
dos=0
tre=0
qtr=0
cin=0
sei=0
cont=0
while cont!=100:
    var=random.randint(1,6)
    if var==1:
        uno+=1
    if var==2:
        dos+=1
    if var==3:
        tre+=1
    if var==4:
        qtr+=1
    if var==5:
        cin+=1
    if var==6:
        sei+=1
    cont+=1
else:
    print("Uno: ",uno )
    print("Dos: ",dos)
    print("Tres: ",tre)
    print("Cuatro: ",qtr)
    print("Cinco: ",cin)
    print("Seis: ",sei)
    