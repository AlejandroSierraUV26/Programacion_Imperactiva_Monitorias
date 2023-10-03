import random
for i in range(0,10):
    while(True):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        if n1 == 3 and n2 == 5 or n1 == 5 and n2 ==3:
            continue
        else:
            break
        

    resultado = n1 * n2

    print("¿Cuánto es", n1, "por", n2, "?")

    respuesta_correcta = int(input("Ingrese la respuesta : "))

    if respuesta_correcta == resultado:
        print("¡Respuesta correcta!")
    else:
        print("¡Respuesta incorrecta!")
        print("La respuesta correcta es", resultado)



