from PROGParcial_Fcs import *
adn = []
count = 1
b = 3
while True:
    adn_aux = str(input(f"Ingrese cadena de ADN número {count}, necesita una longitud de 6 y solo puede contener los carácteres A, T, C y G:\n"))
    adn_aux = adn_aux.upper()
    if check(adn_aux):
        adn.append(adn_aux)
        count += 1
    else:
        print("Cadena inválida")
    if count > 6:
        break
for b in range(1,4):
    print(is_mutant(adn,b))
print(adn)