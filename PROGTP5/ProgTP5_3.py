#Sé que lo más inteligente sería hacer un archivo con todas las funciones pero lo hago de esta manera para poder comentar cada proceso
from ProgTP5_Funciones import valid
while True:
    name = str(input("Ingrese su nombre completo, ingrese un espacio vacío para finalizar\nSi tiene múltiples nombres puede ingresarlos separados, pero solo un apellido\n"))
    if name == "":
        break
    dni = int(input("Ingrese su DNI:\n"))
    if valid(dni):
        dni = str(dni)
        first_name = (name[0:name.find(" ")])
        last_name = (name[name.rfind(" ") + 1:len(name)])
        short_dni = dni[0:3]
        unique_id = first_name + str(len(last_name)) + short_dni
        print(unique_id)