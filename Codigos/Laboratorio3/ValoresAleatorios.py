import random
import numpy as np
from tabulate import tabulate
nombres = ["Alejandro","Maria","Carlos","Juan","Juana","Valentina","Jessica","Daniela"]
apellidos = ["Sierra","Lopez","Martinez","Torrez","Velasco","Hernandez"]
personas = []
for i in range(100):
    personas.append([])
    numero_nombre = random.randint(0,len(nombres)-1)
    numero_apellidos = random.randint(0,len(apellidos)-1)
    nombre_completo = nombres[numero_nombre] +" "+ apellidos[numero_apellidos]
    personas[i].append(nombre_completo)

personas = np.array(personas)

print(tabulate(personas, headers= ["Nombre Completo"]))    