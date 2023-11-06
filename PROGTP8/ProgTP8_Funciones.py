#Importamos math para usar la función trunc
import math
#Definimos la función que va a recibir el número y el contador (No se puede inicializar el contador en la función)
#debido a que al ser recursiva se inicializaría varias veces
def count_digs(n, c):
    #Dividimos el número en diez y lo truncamos
    n /= 10
    math.trunc(n)
    #Si esto resulta en un número mayor o igual a uno, añadimos un dígito a la función y volvemos a llamarla
    if n >= 1:
        c += 1
        return count_digs(n, c)
    #Si no resulta en un número mayor o igual a uno, significa que al dividirlo estábamos en el último dígito, por lo que devuelve la cuenta total de dígitos
    else:
        return c

#Definimos la funcion exp que recibe los dos números y el contador
def exp(n, b, a, c):
    #Si el primer número es superior al segundo, se multiplica por el auxiliar y se añade uno al contador
    if n > b:
        b = b * a
        c += 1
        #Después de eso volvemos a llamar la funcipon pasándole todos los recursos
        return exp(n, b, a, c)
    #Si en una de las recursiones n y b se igualan significa que n es potencia de b y se devuelve True junto al contador
    elif n == b:
        return True, c
    #Si b llega a superar a n significa que esta no era potenci y se devuelve false
    elif b > n:
        return False

#Definimos la función que vamos a usar para comprobar si string está en string
def str_in_str(a,b,lst,c):
    if b in a:
        fnd = (a.find(b)) + 1
        lst.insert(c, fnd)
        c += 1
        a = a[fnd + (len(b) - 1): len(a)]
        return str_in_str(a,b,lst,c)
    else:
        c2 = 1
        for c2 in range(1, len(lst)):
            lst[c2] += lst[(c2-1)]
            lst[c2] += (len(b) - 1)
        return lst

#Definimos la función impar
def odd(n, s, a):
    #Al ser la primera llamada ve si el número es uno, si lo es, devuelve impar
    if n == 1:
        s = "impar"
        return s
    elif n != 1 and n != abs(a):
        #Si no es uno, asume que el número es par y disminuye el auxiliar en uno
        s = "par"
        a -= 1
        #Llama a la función par con los valores actualizados
        return even(n, s, a)
    #Si la función es igual al valor absoluto del auxiliar, que como inicializó en uno y fue alternando a la vez que
    #El string, al llegar a este punto s tiene el valor correspondiente al número
    elif n == abs(a):
        return s

#Definimos la función par que tiene el mismo comportamiento que impar sin el chequeo inicial de si es uno
def even(n, s, a):
    if n != abs(a):
        s = "impar"
        a -= 1
        return odd(n, s, a)
    elif n == abs(a):
        return s