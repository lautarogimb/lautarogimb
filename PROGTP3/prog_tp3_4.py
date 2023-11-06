# Pedimos al usuario un número comprobando que sea positivo
while True:
    num = int(input("Ingresa un número: "))
    if num >= 0:
        break
# Hacemos un bucle for con paso -1 para que vaya atrás
for count in range((num), -1, -1):
    # Hacemos un if y else para añadir comas donde es necesario
    if count == 0:
        print(f"{count}" , end=" ")
    else:
        print(f"{count}, " , end=" ")