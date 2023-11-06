#Bueno profe este lo iso bastante tarde me quedó un poco caótico el código pero funcionar funciona
#Definimos las variables a usat
nonprime = 0
prime = 0
num = -1
#Hacemos un bucle infinito del que salir con un break
while True:
    #Hacemos que solo pueda salir ingresando un bucle igual o mayor que cero
    while num < 0:
        num = int(input("Ingrese un número mayor a 0, o 0 para terminar el bucle\n"))
    #Ponemos el break en caso de 0
    if num == 0:
        break
    #Hacemos un bucle que cuenta cuando se encuentra un divisor, al final de este en caso de no encontrar ninguno se añade uno al contador de números primos
    for count in range(2 , num - 1):
        if (count != num) and (num % count) == 0:
            nonprime += 1
    if nonprime == 0:
        prime += 1
    #Reseteamos las variables para que vuelva a iniciarse el bucle
    nonprime = 0
    num = -1
#Imprimimos la cantidad de números primos
print(f"La cantidad de números primos ingresados es de {prime}")