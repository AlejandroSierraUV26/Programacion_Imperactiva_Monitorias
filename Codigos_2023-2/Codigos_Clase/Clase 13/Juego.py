import random

def jugar_ronda(dificultad, max_intentos):
    if dificultad == 1:
        numero_secreto = random.randint(1,10)
        dificultad = 10
    elif dificultad == 2: 
        numero_secreto = random.randint(1, 50)
        dificultad = 50
    elif dificultad == 3:
        numero_secreto = random.randint(1, 100)
        dificultad = 100
    print(f"Ronda - Adivina el número entre 1 y {dificultad} en {max_intentos} intentos.")
    print("Número secreto generado. Comienza a adivinar.\n")

    intentos = 0
    puntos = 0

    while intentos < max_intentos:
        intento = int(input(f"Intento #{intentos + 1}: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado en el intento #{intentos}.")
            puntos += (max_intentos - intentos + 1) * 10
            print(f"Ganaste {puntos} puntos.\n")
            return puntos

        elif intento < numero_secreto:
            print("El número secreto es mayor.\n")
        else:
            print("El número secreto es menor.\n")

    print(f"Agotaste tus {max_intentos} intentos. El número secreto era {numero_secreto}.\n")
    return puntos




if __name__ == "__main__":
    print("¡Bienvenido al Juego de Adivinanza Avanzado!\n")

    while True:
        print("Elige el nivel de dificultad:")
        print("1. Fácil (rango de 1 a 10)")
        print("2. Medio (rango de 1 a 50)")
        print("3. Difícil (rango de 1 a 100)")

        dificultad = 0
        while dificultad not in [1, 2, 3]:
            try:
                dificultad = int(input("Elige el nivel de dificultad (1/2/3): "))
            except ValueError:
                print("Ingresa una opción válida.")

        max_intentos = 5  

        puntos_acumulados = 0
        ronda = 1
        while True:
            print(f"\nRonda {ronda} - Dificultad: 
                  {'Fácil' if dificultad == 1 else 'Medio' if dificultad == 2 else 'Difícil'}")
            puntos_acumulados += jugar_ronda(dificultad , max_intentos)
            ronda += 1

            respuesta = input("¿Deseas jugar otra ronda? (Sí/No): ").lower()
            if respuesta != 'sí':
                break

        print(f"\nPuntuación final: {puntos_acumulados} puntos. ¡Gracias por jugar!")

        respuesta = input("¿Deseas jugar de nuevo? (Sí/No): ").lower()
        if respuesta != 'sí':
            break

