lis=[]
var=input("Introduce una letra: ")
if var.isalpha():
    lis.append(var)
   
sin=input("Quieres introducir otra letra? s/n ")
while sin!="n":
    var=input("Introduce una letra: ")
    if var in "áà":
        var="a"
    elif var in "éè":
        var="e"
    elif var in "íì":
        var="i"
    elif var in "óò":
        var="o"
    elif var in "úù":
        var="u"
    if var.isalpha():
        lis.append(var)
    sin=input("Quieres introducir otra letra? s/n ")
print(set(lis))