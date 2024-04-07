# i = 2 #! Se inicializa el contador en 2
# numero = 7 #! Se define el numero a evaluar
# contador = 0 #! Se inicializa el contador en 0
# while i<numero:
#     if numero % i == 0:
#         contador+=1 #? Se incrementa el contador en 1 si es que el numero es divisible por i
#     i+=1 #? Se incrementa el contador en 1
# if contador == 0: #? Si el contador es 0, el numero es primo
#     print("El numero es primo")
# else:
#     print("El numero no es primo")
    

# Diseñar una funcion que cumpla con la secuencia
"""

"""



# n = int(input("Ingrese un numero: "))

# i = 1
# print(i)
# while i <= n:
#     if i % 4 == 0:
#         print(i)
#     i+=1



# def orderRecursiva(Arreglo, posicion, pasos):
#     print(f"Posicion : {posicion} |", end=" ")
#     for i in range(0, len(Arreglo)):
#         print(Arreglo[i], end="|")
#     print()
#     if posicion > 1:
#         for j in range(0, len(Arreglo)):
#             if j+1 < len(Arreglo):
#                 if Arreglo[j] > Arreglo[j+1]:
#                     temp = Arreglo[j]
#                     Arreglo[j] = Arreglo[j+1]
#                     Arreglo[j+1] = temp
#                     pasos += 1
#         pasos = orderRecursiva(Arreglo, posicion-1, pasos)
#     return pasos

# def order(Arreglo):
#     pasos = orderRecursiva(Arreglo, len(Arreglo), 0)
#     return Arreglo, pasos

# arreglo = [13,3,4,12,14,10,5,1,8,2]
# ordenado, pasos = order(arreglo)

# print(ordenado)
# print("Pasos realizados: ", pasos)


# mostrar el recorrido de la secuencia de collatz


def collatz(n):
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return collatz(n/2)
    else:
        return collatz(3*n+1)


collatz(10)
    