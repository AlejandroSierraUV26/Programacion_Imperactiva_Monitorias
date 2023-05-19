"""
Ejercicio 3.
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 
22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

"""

#*Lista definida
lista = [50,75,46,22,80,65,8]

#!Hallar el mayor
def mayor(lista):
    mayor = 0
    for i in range(0,len(lista)):
        if mayor < lista[i]:
            #* 80 < 8
            mayor = lista[i]
    return mayor

#!Hallar el menor
def menor(lista):
    menor = 100
    for i in range(0,len(lista)):
        if menor > lista[i]:
            menor = lista[i]
    return menor
print("Menor : ")
print(menor(lista))
print("Mayor : ")
print(mayor(lista))