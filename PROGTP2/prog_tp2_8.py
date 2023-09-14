user = "Gwenevere"
passw = "excalibur"
string = input("Ingrese el usuario: ")
if string == user:
    string = input("Ingrese la contraseña: ")
    if string == passw:
        print("Usuario y contraseña correctos")
    else:
        print("Valor incorrecto")
else:
    print("Valor incorrecto")