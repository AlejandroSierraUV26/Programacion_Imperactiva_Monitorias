"""

Ejercicio 2.
Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.


"""
#*Inicio
lista = []

#*Almacenamos

for i in range(1,10+1):
    lista.append(i)

#![1,2,3,4,5,6,7,8,9,10]
#*Invertimos
lista.reverse()
#*[10,9,8,7,6,5,4,3,2,1]

for i in range(0,len(lista)):
    print(f"{lista[i]} ,", end ="")