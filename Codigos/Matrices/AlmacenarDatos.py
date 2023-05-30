import numpy as np

def mayor(arreglo):
    mayor = 0
    for i in range(0,len(arreglo)):
        if mayor < arreglo[i][1]:
            mayor = arreglo[i][1]
            indice = i
    return indice

def menor(arreglo):
    menor = 100
    for i in range(0,len(arreglo)):
        if menor > arreglo[i][1]:
            menor = arreglo[i][1]
            indice = i
    return indice

arreglo = []

for i in range(3):
    arreglo.append([])
    nombre_ciudad  = str(input(f"Ingrese el nombre de la ciudad {i+1} :"))
    temp_ciudad  = float(input(f"Ingrese el temperatura de la ciudad {i+1} :"))
    arreglo[i].append(nombre_ciudad)
    arreglo[i].append(temp_ciudad) 
print(f"La ciudad con mayor temperatura es : {arreglo[mayor(arreglo)][0]}\n La tempertura es : {arreglo[mayor(arreglo)][1]}")
print(f"La ciudad con menor temperatura es : {arreglo[menor(arreglo)][0]}\n La tempertura es : {arreglo[menor(arreglo)][1]}")

arreglo = np.array(arreglo)
print(arreglo)




