#Pedimos al usuario que entre líneas
print("Ingrese una secuencia de líneas, para terminar la secuencia ingrese un epacio vacío")
#Hacemos el ciclo donde pedimos que ingrese líneas
while True:
    print("Ingrese una línea")
    line = str(input())
    #Hacemos un break en caso de un espacio vacío
    if line == "":
        print("Ciclo terminado")
        break
    #Imprimimos la línea ingresada en mayúsculas
    print(line.upper())