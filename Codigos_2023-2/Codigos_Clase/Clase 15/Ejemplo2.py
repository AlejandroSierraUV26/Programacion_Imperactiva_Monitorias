import numpy as np
from tabulate import tabulate 

matrix = [
    ["Alejandro","Sierra",19],
    ["Santiago", "Hernandez",23],
    ["Samuel", "Valdes", 17]
]

# Mostrar los nombres  de cada persona

# for i in range(0, len(matrix)):
#     print(matrix[i][0])

# Agregar persona nueva

# nombre = str(input("Ingrese el nombre : "))

# apellido = str(input("Ingrese el apellido : "))

# edad = int(input("Ingrese la Edad : "))

# matrix.append([])
# matrix[-1].append(nombre)
# matrix[-1].append(apellido)
# matrix[-1].append(edad)

matrix = np.array(matrix)

print(tabulate(matrix, headers=["Nombre", "Apellido", "Edad"]))




