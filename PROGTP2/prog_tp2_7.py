print("Ingrese tres números: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())
mayor = 0
if num1 > mayor:
    mayor = num1
    if num2 > mayor:
        mayor = num2
        if num3 > mayor:
            mayor = num3
print(f"El número mayor es {mayor}")