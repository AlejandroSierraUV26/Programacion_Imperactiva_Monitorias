import numpy as np 
from tabulate import tabulate
titulos = ['Nombre','Edad']
matrix = [["Alejandro",18],["Juan",20],["Maria",18],["Camilo",18],["Pedro",10],["Jose",11],["Camila",19]]
matrix = np.array(matrix)
promedio = 0
for i in range(len(matrix)):
    promedio +=(int(matrix[i][1]))/len(matrix)
for j in range(len(matrix)):
    if int(matrix[j][1]) <= promedio:
        print(matrix[j][0])
print(tabulate(matrix, headers=titulos,tablefmt='fancy_grid'))

#Se tiene la edad de el grupo 50 
#Se quiere verificar quien esta fuera del promedio 
#imprimir el nombre de quien esta fuera de este.


# Alejo---21
# Maria ---18
# Juan ---18
# Camilo---20
# Pedro---10
# Jose ---11
# Camila ---19
