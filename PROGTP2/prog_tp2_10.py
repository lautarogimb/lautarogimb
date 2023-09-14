age = int(input("Ingrese su edad: "))
if age < 4:
    print("La entrada es gratis")
elif age < 18:
    print("La entrada cuesta $500")
else:
    print("La entrada custa $1000")