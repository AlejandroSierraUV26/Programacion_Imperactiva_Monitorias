import numpy as np
from tabulate import tabulate
matrix = []

for i in range(0,10):
    matrix.append([])
    matrix[i].append("Alejandro")
    matrix[i].append((19 * i )+ 1)
    
matrix = np.array(matrix)
print(tabulate(matrix, headers=["Nombre","Edad"], showindex="always"))


