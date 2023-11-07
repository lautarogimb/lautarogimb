#Esto definitivamente se puede hacer con un bucle for pero se me complicó
from ProgTP7_3Fnc import sort_dct
lst = [{'1':"", '2':"", '3':""},
{'1':"", '2':"", '3':""},
{'1':"", '2':"", '3':""},
{'1':"", '2':"", '3':""}]
for count in range(0,4):
    print(f"libro {count + 1}")
    lst[count]['1'] = str(input("Ingrese el nombre del libro:"))
    lst[count]['2'] = str(input("Ingrese el autor del libro:"))
    lst[count]['3'] = int(input("Ingrese el año de salida del libro:"))
count = 0
lst = sort_dct(lst)
print("Los libros ordenados en cuanto a su fecha de lanzamiento son:")
for count in range(0,4):
    print(f"{(lst)[count]['1']}, salido en {(lst)[count]['3']}")