from Fcs_ordenamiento import insertion_sort
lst = list()
while True:
    wrd = str(input("Ingrese una palabra o un espacio vacío para salir del ciclo: \n"))
    if wrd == "":
        break
    lst.append(wrd)
insertion_sort(lst)
print("Las listas ordenadas son:")
for count in range(0, len(lst)):
    print(lst[count])