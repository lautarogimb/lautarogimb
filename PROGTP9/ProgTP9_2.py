class Cuenta:

    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def getter_name(self):
        return self.__name

    def setter_name(self, name):
        self.__name = name

    def getter_quantity(self):
        return self.__quantity

    def setter_quantity(self, quantity):
        self.__quantity = quantity

    def mostrar(self):
        print(f"Nombre: {self.__name}\nDinero: {self.__quantity}")
        if self.__quantity < 0:
            print("¡Números rojos!")

    def ingresar(self,quantity):
        if quantity > 0:
            self.__quantity += quantity
            print(f"Se ha ingresado {quantity} a su cuenta")
        else:
            print("Número inválido")

    def retirar(self,quantity):
        if quantity > 0:
            self.__quantity -= quantity
            print(f"Se ha retirado {quantity} de su cuenta")
        else:
            print("Número inválido")

nombre = str(input("Ingrese un nombre: "))
cantidad = int(input("Ingrese la cantidad de dinero que tiene su cuenta: "))
cuenta = Cuenta(nombre, cantidad)
while True:
    num= int(input("Ingrese un número para hacer una operación\n1: Mostrar cuenta\n2: Ingresar dinero\n3: Retirar dinero\n4: Salir del bucle\n"))
    if num == 1:
        cuenta.mostrar()
    elif num == 2:
        cantidad = int(input("Ingrese la cantidad de dinero a mover: "))
        cuenta.ingresar(cantidad)
    elif num == 3:
        cantidad = int(input("Ingrese la cantidad de dinero a mover: "))
        cuenta.retirar(cantidad)
    elif num == 4:
        break
    else:
        print("Número inválido")