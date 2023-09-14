num = int(input("Ingrese un año: "))
if num % 400 == 0:
    print("El año es bisiesto")
elif num % 4 == 0 and num % 100 != 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")