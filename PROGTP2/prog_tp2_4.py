vote = input("¿Por qué candidato quere votar? A: Pepe, Equipo rojo, B: Juan, Equipo verde, C: Manuel, Equipo azul: ")
if vote == "A" or "a":
    print("Usted ha votado por el partido rojo")
elif vote == "B" or "b":
    print("Usted ha votado por el partido verdad")
elif vote == "C" or "c":
    print("Usted ha votado por el partido azul")
else:
    print("Voto no válido")