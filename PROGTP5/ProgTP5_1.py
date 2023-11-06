#Definimos la función para validar el DNI
def valid(par_num):
    count = 0
    #Hacemos un bucle while que divide el número hasta que sea menor a uno contando cada vez que se ejecuta para ver el número de dígitos
    while par_num >= 1:
        par_num /= 10 
        count += 1
    #Al salir del bucle comprobamos si se contaron 7 u 8 dígitos y asignamos el resultado
    if count == 7 or count == 8:
        return True
    else:
        return False
#El bloque principal del cpodigo que pide el número y llama a la función
num = int(input("Ingrese un número de DNI: "))
if valid(num):
    print("El número de DNI es válido")
else:
    print("El número de DNI no es válido")