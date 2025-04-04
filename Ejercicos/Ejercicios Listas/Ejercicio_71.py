lis=[]
var=input("Introduce una letra: ")
if var.isalpha():
    lis.append(var)
   
sin=input("Quieres introducir otra letra? s/n ")
while sin!="n":
    var=input("Introduce una letra: ")
    if var.isalpha():
        lis.append(var)
    sin=input("Quieres introducir otra letra? s/n ")
print(set(lis))
    
    
    