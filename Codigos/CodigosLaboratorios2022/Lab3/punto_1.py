"""
punto #1
laboratorio 4

integrantes:

Alejandro Sierra Betancourt-2259559
Tina María Torres-2259729
Edgar Rueda Colonia-2259606
Kevin Steven Ramírez-2259371

profesor: Carlos Delgado
3743

"""
import numpy as np
from collections import Counter
def productoEstrella(n_dias):
    arreglo = np.array([])
    mayor = np.array([])
    mayor2 = np.array([])
    for j in range(1,n_dias+1):
        cd = int(input(f"Ingrese el codigo del producto estrella del dia {j} : "))
        arreglo = np.insert(arreglo,arreglo.shape[0],cd)
    if len(arreglo)==len(set(arreglo)): 
        return ("No hubo producto estrella por esos meses")
    else: 
        for i in range(0,arreglo.shape[0]):
            if arreglo[i] == Counter(arreglo).most_common(2)[0][0]:
                mayor = np.insert(mayor,mayor.shape[0],i+1)
            if arreglo[i] == Counter(arreglo).most_common(2)[1][0]:
                mayor2 = np.insert(mayor2,mayor2.shape[0],i+1)
        return (f"--------------------------------------------------------------------\nEl producto estrella que más se repite es el : {int(Counter(arreglo).most_common(2)[0][0])}\nSe repite en total : {Counter(arreglo).most_common(2)[0][1]} veces\nDonde más se repite es en los dias : {mayor}\n--------------------------------------------------------------------\nEl segundo producto estrella que más se repite es el : {int(Counter(arreglo).most_common(2)[1][0])}\nSe repite en total : {Counter(arreglo).most_common(2)[1][1]} veces\nDonde más se repite es en los dias : {mayor2}\n--------------------------------------------------------------------\nLista :  {arreglo}")
n_dias = int(input("Ingrese el total de dias vendidos : "))
print(productoEstrella(n_dias))
#11 16 19 11 17 13 19 19 13 12 11 19 15 14 14 18 18 16 17 12