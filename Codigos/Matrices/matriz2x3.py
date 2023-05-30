import numpy as np
from tabulate import tabulate
matrix = [["Alejandro",18,"Rojo"]
          ,["Maria",19,"Azul"]
          ,["Carlos",40,"Blanco"]]
matrix = np.array(matrix)

promedio = 0

for i in range(len(matrix)):
    promedio += int(matrix[i][1])/len(matrix)
for j in range(len(matrix)):
    if (int(matrix[j][1])<=promedio):
        print(matrix[j][0])
















titulos = ["Nombre","Edad","Color Favorito"]
# print(tabulate(matrix, headers=titulos))

















#? pip install numpy
#* pip install tabulate
"""
Realizar un programa que muestre quienes estan por debajo del promedio
y mostrarlos con su nombre, utilizar el mismo codigo con los mismos datos.

"""
# print(f"Nombre : {matrix[0][0]}")
# print(f"Edad : {matrix[0][1]}")