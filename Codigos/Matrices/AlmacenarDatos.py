import numpy as np

arreglo = []

for i in range(2):
    arreglo.append([])
    nombre_ciudad  = str(input(f"Ingrese el numero de la  :"))
    temp_ciudad  = float(input(f"Ingrese el temperatura de la ciudad :"))
    arreglo[i].append(nombre_ciudad)
    arreglo[i].append(temp_ciudad)
arreglo = np.array(arreglo)
print(arreglo)


[["Alejandro",18],["Maria",20]]

#? Crear un arreglo que almacene el nombre de la materia y la nota final 
#? 3 Materias y mostrarlas con el tabulate


