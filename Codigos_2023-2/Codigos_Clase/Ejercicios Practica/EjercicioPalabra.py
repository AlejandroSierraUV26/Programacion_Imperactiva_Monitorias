"""

A partir de una palabra ingresada por el usuario, mostrar 
por pantalla la misma palabra pero con las letras ordenadas alfabéticamente.	



"""

import random

def desorganizar_cadena(cadena):
    # Convierte la cadena en una lista de caracteres
    caracteres = list(cadena)
    
    # Mezcla aleatoriamente los caracteres
    random.shuffle(caracteres)
    
    # Convierte la lista de caracteres nuevamente en una cadena
    cadena_desorganizada = ''.join(caracteres)
    
    return cadena_desorganizada

palabras = ["hola", "mundo", "python", "programacion", "universidad", "computacion"]

palabra = random.choice(palabras)


palabraelegida = desorganizar_cadena(palabra)
contador = 0
while True:
    print(palabraelegida)
    palabraingresada = input("Ingrese la palabra: ")
    if palabraingresada == palabra:
        print("Correcto")
        break
    else:
        print("Incorrecto")
        print("Intente nuevamente")
        contador +=1
        if(contador ==5):
            print("Perdiste")
            break



