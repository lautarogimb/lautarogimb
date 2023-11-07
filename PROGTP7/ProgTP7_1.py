from Fcs_ordenamiento import bubble_sort
lst = list()
num = 1
count = 0
while True:
    num = int(input("Ingrese un número para el arreglo o 0 para cerrarlo:\n"))
    if num == 0:
        break
    lst.insert(count, num)
    count += 1
bubble_sort(lst)
print(lst)