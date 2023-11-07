class Persona:

    def __init__(self, name, age, dni):
        self.__name = name
        self.__age = age
        self.__dni = dni

    def getter_name(self):
        return self.__name

    def setter_name(self, name):
        self.__name = name

    def getter_age(self):
        return self.__age

    def setter_age(self, age):
        self.__age = age

    def getter_dni(self):
        return self.__dni

    def setter_dni(self, dni):
        self.__dni = dni

    def mostrar(self):
        print(f"Nombre: {self.__name}\nEdad: {self.__age}\nDNI: {self.__dni}")

    def esMayorDeEdad(self):
        if self.__age >= 18:
            return True
        else:
            return False

nombre = str(input("Ingrese un nombre: "))
edad = int(input("Ingrese su edad: "))
dni = int(input("Ingrese su DNI: "))
persona = Persona(nombre, edad, dni)

persona.mostrar()