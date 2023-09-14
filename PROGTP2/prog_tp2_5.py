let = input("Ingrese una letra: ")
let.lower()
if len(let) > 1:
    print("No se puede evaluar el valor ingresado")
elif let == "a" or let == "e" or let == "i" or let == "o" or let == "u":
    print("La letra ingresada es vocal")
else:
    print("La letra ingresada no es vocal")