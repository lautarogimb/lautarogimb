from ProgTP8_Funciones import exp
#El código principal, donde declaramos las variables y llamamos la función
count = 1
num = int(input("Ingrese un número:\n"))
num2 = int(input("Ingrese otro número:\n"))
#Creamos una variable auxiliar con el valor de 5 para poder hacer la potencia bien
aux = num2
#Si la función retorna true el código imprime el resultado incluyendo el segundo valor de retorno, si no simplemente imprime el resultado
if exp(num, num2, aux, count):
    print(f"{num} es {num2} elevado a {exp(num, num2, aux, count)[1]}")
else:
    print(f"{num} no es un exponente de {num2}")