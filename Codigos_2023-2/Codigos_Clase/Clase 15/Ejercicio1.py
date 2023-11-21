import numpy as np 

matrix = [
    ["",0],
    ["",0],
    ["",0],
    ["",0],
    ["",0]
    
]

matrix[0][0] = "Alejandro"
matrix[0][1] = 19


for i in range(0, len(matrix)):
    matrix[i][0] = input("Ingrese el nombre: ")
    matrix[i][1] = int(input("Ingrese la edad: "))




matrix = np.array(matrix)

print(matrix)