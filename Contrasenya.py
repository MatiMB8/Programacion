print("Instruccions")
print("1. La longutud del password te que tenir entre 6 i 8 caracters")
print("2. Forzar els seguents valors segons la posició indicada:")
print("Posicio 1 Un numero mayor o igual a 1 i menor o igual a 5")
print("Posicio 2 Una lletra minuscula")
print("Posicio 3 Una lletra mayuscula")
print("Posicio 4 Un dels seguents simbols * _  @")
print("Posicio 5 Una lletra minuscula")
print("Posicio 6 Un numero mayor o igual a 6 o menor o igual a 9")
print("Posicio 7 Un dels seguents simbols & / #")
print("Posicio 8 Un numero menor o igual a 5")

password=input("Introduce una palabra clave: ")
var=len(password)
mal = False

if var < 6 or var > 8:
    print("Error, el password té una longitud de ", var, " caràcters i no compleix els requisits")
    mal = True
else:
    if not password[0].isdigit() or not (1 <= int(password[0]) <= 5):
        print("Error en el primer caracter")
        mal = True
    if not password[1].islower():
        print("Error en el segundo caracter")
        mal = True
    if not password[2].isupper():
        print("Error en el tercer caracter")
        mal = True
    if password[3] not in "_*@":
        print("Error en el cuarto caracter")
        mal = True
    if not password[4].islower():
        print("Error en el quinto caracter")
        mal = True
    if len(password) > 5 and (not password[5].isdigit() or not (6 <= int(password[5]) <= 9)):
        print("Error en el sexto caracter")
        mal = True

if var == 7:
    if password[6] not in "#%/":
        print("Error en el séptimo caracter")
        mal = True
elif var == 8:
    if not password[7].isdigit() or not (0 <= int(password[7]) <= 5):
        print("Error en el último caracter")
        mal = True

if not mal:
    print("El format del PASSWORD és correcte")

