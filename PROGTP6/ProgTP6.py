#Definimos las variables y listas a usar
num, count, addition = 1, 0, 0
vlist, vlist2 = list(), list()

#Hacemos un bucle que comprueba si el número es distinto a cero y si lo es añade el número a la lista
while num != 0:
    num = int(input("Ingrese un número, o 0 para salir del bucle: \n"))
    if num != 0:
        vlist.insert(count, num)
    count += 1
count = 0

#Le pedimos al usuario que ingrese un número y si ese número está en la lista lo eliminamos
num = int(input("Ingrese un número para eliminar: \n"))
if num in vlist:
    del vlist[vlist.index(num)]

#Hacemos un bucle que añada todos los valores de la lista y lo imprimimos por pantalla
while count < len(vlist):
    addition += vlist[count]
    count+= 1
count = 0
print(f"La adición de su lista termina en {addition}")

#Hacemos el bucle que al ingresar un número, si el valor de la lista es mayor lo añade a una segunda lista
num = int(input("Ingresa un número: \n"))
while count < len(vlist):
    if num < vlist[count]:
        vlist2.insert(count, vlist[count])
    count += 1
count = 0

#Imprimimos la lista de los números mayores
print("La lista con todos los números mayores al ingresado es: ")
while count < len(vlist2):
    print(vlist2[count])
    count += 1