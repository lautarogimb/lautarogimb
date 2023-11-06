#Hacemos la función para encontrar la palabra más larga 
def find_longest(par_phrase):
    #Hacemos que reemplace las comas por espacios vacíos para que no molesten, se podría hacer con otros signos pero las comas son las más comunes
    par_phrase = par_phrase.replace(",","")
    #Inicializamos la variable longest fuera del ciclo
    longest = ""
    #Hacemos un bucle que termina si la longitud de la frase es 0
    while len(par_phrase) != 0:
        #Hacemos la variable espacio cuyo valor es el del índice del primer espacio encontrado, adicionalmente, si no se encuentra ninguno su índice es el final de la frase
        space = par_phrase.find(" ")
        if space == -1:
            space = len(par_phrase)
        #Hacemos un auxiliar que guarda una palabra
        aux = par_phrase[0:space]
        #Si la palabra auxiliar es más larga que la actualmente más larga, esta la reemplaza
        if len(aux) > len(longest):
            longest = aux
        #Hacemos que la frace ahora se inicializa desde después del último espacio
        par_phrase = par_phrase[space + 1:]
    print(f"La palabra más larga es {longest}")
#El código principal donde pedimos la frase y llamamos la función
phrase = str(input("Ingrese una frase\n"))
find_longest(phrase)