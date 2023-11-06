def mult(par_num, par_num2):
    if par_num % par_num2 == 0:
        return True
    else:
        return False
num1 = int(input("Ingresa dos números:\n"))
num2 = int(input())
if mult(num1, num2):
    print("El segundo número es múltiplo del primero")
if mult(num2, num1):
    print("El primer número es múltiplo del segundo")
if not mult(num1, num2) and not mult(num2, num1):
    print("Los números no son múltiplos entre ellos")