# Pedimos al usuario un número comprobando que sea positivo
while True:
    num = int(input("Ingresa un número: "))
    if num >= 0:
        break
# Hacemos un bucle for con paso 2 para que solo cuente impares
for count in range(1, (num + 1), 2):
    # Hacemos un if y else para añadir comas donde es necesario
    if count == num:
        print(f"{count}" , end=" ")
    else:
        print(f"{count}, " , end=" ")