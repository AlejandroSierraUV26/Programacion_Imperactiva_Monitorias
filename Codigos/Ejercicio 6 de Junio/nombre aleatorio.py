import numpy as np
import random
from tabulate import tabulate

nombres = ["Alejandro","Maria","Carlos","Daniel","Karen","Juan","Camilo","Camila","Juana","Martha","Isabela","Valentina"]
apellido = ["Sierra","Muñoz","Rodriguez","Gutierrez","Ramirez","Lopez","Flores","Hernandez"]


for i in range(50):
    numero_nombre = random.randint(0,len(nombres)-1)
    numero_apellido = random.randint(0,len(apellido)-1)
    nombre_completo = nombres[numero_nombre] +" "+ apellido[numero_apellido]
    edad = random.randint(1,80)
    print(nombre_completo)
    print(f"Edad : {edad}")
    print()
    
    
    