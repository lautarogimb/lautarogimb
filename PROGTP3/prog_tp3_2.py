#Le pedimos la edad al usuario
age = int(input("Ingrese su edad: "))
#Hacemos el ciclo con rango de 1 a su edad actual más uno para imprimir la cantidad de veces que cumplió años
for count in range(1,(age + 1)):
    print(f"Ha cumplido {count} años")