#Definimos el número principal que será modificado dentro del bucle
num = 0
#Hacemos un bucle infinito del que se saldrá con un break
while True:
    #Pedimos que ingrese la transacción entera
    tran = str(input(f"Ingrese un número acompañado de D o R para Depositar o Retirar respectivamente, ejemplo, 'D 100', introduzca una línea vacía para finalizar\n"))
    #Comprobamos si está vacía para salir y mostrar por pantalla el estado de la cuenta
    if tran == "":
        print(f"Su cuenta ha finalizado con {num}")
        break
    #Creamos las variables op y amount a partir de subcadenas de la transacción principal que almacenan la operación hecha y la cantidad de dinero en ella
    op = (tran[:1]).lower()
    amount = int(tran[2:])
    #Comprobamos la operación usada y modificamos num acorde a esta
    if op == "d":
        num += amount
        print(f"Ha depositado {amount} en su cuenta")
    elif op == "r":
        num -= amount
        if num < 0:
            #Añadimos un detalle que no se pidió en la consigna pero vale la pena
            print(f"Ha retirado {amount} de su cuenta, se encuentra en deuda con el banco")
        else:
            print(f"Ha retirado {amount} de su cuenta")
    else:
        print("Operación incorrecta")
    #Le imprimimos al usuario la cantidad en su cuenta antes de que se repita el bucle y haga la misma operación
    print(f"Su cuenta actualmente tiene {num}")