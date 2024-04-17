import random
import os

IMAGENES_AHORCADO = ['''
   +---+
   |   |
       |
       |
       |
       |

=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
os.system('cls')
palabras = ['python', 'programacion', 'juego', 'computadora', 'tecnologia', 'openai', 'inteligencia']
def elegir_palabra(lista_palabras):
    return random.choice(lista_palabras)
def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + ' '
        else:
            tablero += '_ '
    print(tablero)

def jugar_ahorcado():
    print("¡Bienvenido al juego del ahorcado!")
    palabra_secreta = elegir_palabra(palabras)
    letras_adivinadas = []
    intentos_restantes = 0

    while intentos_restantes < 6:
        print(IMAGENES_AHORCADO[intentos_restantes])
        print()
        print("\nIntentos:", intentos_restantes)
        mostrar_tablero(palabra_secreta, letras_adivinadas)

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has ingresado esa letra. Intenta con otra.")
            continue
        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            print("Incorrecto. La letra no está en la palabra secreta.")
            intentos_restantes += 1

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break

    else:
        print(IMAGENES_AHORCADO[intentos_restantes])
        print("\n¡Oh no! Has agotado tus intentos. La palabra era:", palabra_secreta)

jugar_ahorcado()
