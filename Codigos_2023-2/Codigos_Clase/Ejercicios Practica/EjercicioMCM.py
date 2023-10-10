"""

Realizar un programa que calcule dos numeros que multiplicados 
sean el que indica la persona.

Ejemplo 1

>>> Ingresa 20

>>> 20 = 5 * 4

Ejemplo 2

>>> Ingresa 50

>>> 50 = 5 * 10


"""
numero  = int(input("Ingrese el numero a calcular : "))
contador = 0
for i in range(0,numero+1):
    for j in range(0,numero+1):
        if i*j == numero:
            print(f"{numero} = {i} * {j}")
            contador += 1
    else:
        continue
print(contador)

