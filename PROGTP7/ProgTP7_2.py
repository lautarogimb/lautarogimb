from Fcs_ordenamiento import selection_sort
lst = list()
word = ""
count = 0
while True:
    word = str(input("Ingrese una palabra para el arreglo o un espacio vacío para cerrarlo:\n"))
    if word == "":
        break
    lst.insert(count, word)
    count += 1
selection_sort(lst)
print(lst)