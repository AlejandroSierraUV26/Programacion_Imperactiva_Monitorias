
"""
Ejercicio 6 de junio 
Clase 2pm

Boleta ganadora [2,3,1,2,3]


Generar un programa que almace el nombre de una persona 
y el numero apostado al chance, que son 5 numeros, cada 
numero es del 1 al 3.

Indicar que personas ganan con 4 numeros, con un premio 
de 10 millones, si completa las 5 boletas, de 200 millones,
tener en cuenta que si varias personas ganan el mismo premio
debe ser divisible equitativamente para ellos.

Realizarlo para 200 personas. 

Indicar con rojo quien pierde, con amarillo si gana con dos
y verde si gana con tres.


"""
from colorama import init, Fore, Back, Style
import numpy as np
from tabulate import tabulate
print(Fore.RED+"Texto color rojo")
print(Fore.YELLOW+"Texto color amarillo")
print(Fore.GREEN+"Texto color verde")

lista = [[],[],[]]
lista = np.array(lista)
print(tabulate(lista, headers=["texto","color","otro"]))