lis=[]
var=input("Introduce un numero: ")
lis=var.split(".")

if len(lis)==2:
    if lis[0].isnumeric and lis[1].isnumeric():
        print('Es decimal')
    else:
        print("No es decimal")
else:
    print('No es decimal')
