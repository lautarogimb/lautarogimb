num = int(input("Cuántos años tiene su computadora?: "))
if num > 0 and num <= 2:
    print("Su computadora es nueva")
elif num > 2:
    print("Su computadora es vieja")
else:
    print("Error, ha ingresado un número inválido")