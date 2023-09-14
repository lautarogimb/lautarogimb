abc = "abcdefghijklmnñopqrstuvwxyz"
exp = input("Ingrese su nombre")
ini = exp[0]
sex = int(input("Ingrese su sexo 1: Masculino 2: Femenino: "))
if sex != 1 and sex!= 2:
    print("Valor incorrecto")
elif (abc.find((ini)) > 14 and sex == 1) or (abc.find((ini)) <= 14 and sex == 2):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")