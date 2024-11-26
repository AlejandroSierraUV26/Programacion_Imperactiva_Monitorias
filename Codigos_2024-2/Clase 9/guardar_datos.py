import time
import os

nombre = ["Alejandro"]
edad = [16,17,18,19,20]
color = ["red", "blue", "green"]


def guardar_elementos(nombre, edad, color):
    with open("datos.txt", "a") as file:
        file.write(f"{nombre},{edad},{color}\n")
    
def leer_datos(ruta):
    with open(ruta) as file:
        file = file.read() # Leer los datos
        file = file.strip() # elimina los espacios vacios
        file = file.split("\n")  # Separarlos por saltos de lineas
        data = []
        for elem in file:
            elem = elem.split(",")
            data.append(elem)
        for i in range(len(data)):
            data[i][1] = int(data[i][1])
            
    return data    
        

# guardar_elementos(nombre[0], edad[-1], color[1])
datos = leer_datos("datos.txt")





