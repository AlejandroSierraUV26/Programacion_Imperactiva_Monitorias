"""
Operadores Relacionales

*   < Menor
*   > Mayor 
*   <= Menor o igual
*   >= Mayor o igual 
*   == Igual 
*   != Diferente


"""

# Ejemplo 1

num1 = 20

num2 = 50

operacion = num1>num2

#Ejemplo 2

num1 = 20

num2 = 20

operacion = num1<=num2

#Ejemplo 3

edad = 18

edad2 = 19

operacion = edad==edad2
operacion2 = edad!=edad2
print(operacion)
print(operacion2)

"""
Ejercicios: 



Expresar las siguientes expreciones en Python

1. n es mayor que 30

2. n es igual a 60

3. n es mayor o igual que 90



"""

n = int(input("Ingrese un numero: "))

#Punto 1 
print("La operacion es  1: ")
print(n>30)
#Punto 2
print("La operacion es  2: ")
print(n==60)
#Punto 3
print("La operacion es 3 : ")
print(n>=90)
