import random
def adivinar_numero():
    intentos = 0
    limite_inferior = int(input("Ingrese el límite inferior: "))
    limite_superior = int(input("Ingrese el límite superior: "))
    numero = random.randint(limite_inferior, limite_superior)
    respuesta = ""
    while respuesta != "S":
        intentos += 1
        print("El número es", numero, "?")
        print("Rango:", limite_inferior, "-", limite_superior)
        if numero < limite_inferior or numero > limite_superior:
            numero = random.randint(limite_inferior, limite_superior)
        respuesta = input("Ingrese la respuesta (S, A, B): ")
        if respuesta == "A":
            limite_inferior = numero
            numero = random.randint(numero, limite_superior)
        elif respuesta == "B":
            limite_superior = numero
            numero = random.randint(limite_inferior, numero)
    print("El número es", numero)
    print("Intentos:", intentos)
    
adivinar_numero()
