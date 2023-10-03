"""

Realizar un programa que haga una multiplicacion
de 3 numeros y el usuario debera dar la respuesta correcta.
Sino no da la respuesta correcta debera mostrar cual era y seguir
con la siguiente, debe hacerse 10 veces.

"""
import random


def generarNumeros():
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    numero3 = random.randint(1, 10)
    return numero1, numero2, numero3

for i in range(0,10):
    print("Resuelve la multiplicacion de los siguientes numeros: ")
    n1,n2,n3 = generarNumeros()

    multiplicacion = n1*n2*n3
    print(n1,"*",n2,"*",n3,"=")

    resultado = int(input("Ingrese el resultado: "))

    if resultado == multiplicacion:
        print("Ganaste")
        break
    else:
        print("Resultado incorrecto")
        print("El resultado es ", multiplicacion)



