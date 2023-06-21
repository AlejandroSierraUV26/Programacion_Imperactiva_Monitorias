"""
*Realizar un programa que automatice un evento en una sala de cine
*Son en total 45 personas en la sala.

!En principio.

!Debera mostrar el titulo, genero, edad minima, tarifa de entrada.

!Despues de eso un control para la edad.
?Condicion 1:
    Si la persona tiene una edad 
    inferior a la edad minima, 
    se le ubicara en una 
    sala de espera.
    Los demás se les regala un combo de crispetas.
?Condicion 2:
    Si la persona cuenta con el dinero para entrar.
?Condicion 3: 
    
    SOLO si es martes.
    
    Si la persona tiene entre 10 y 20 años paga un 20% menos
    
    Si la personas tiene entre 20 y 30 años pagan un 10% menos
    
    Y si la persona tiene entre 30 y 35 años paga un 5% menos 

!Mostrar la informacion de las personas que estan dentro:

    - Nombre
    - ID
    - Edad
    - Dinero
    - N° Asiento 

!Cuando finalice un reporte por parte de la 
!administracion, que indique 
!las ventas realizadas.

TODO : Es posible llenar los datos con la libreria random






"""

import numpy as np
from tabulate import tabulate
def datos_personas():
    contador = 0
    for i in range(2):
        lista_personas.append([])
        print(f"Cliente {i+1}")
        
        nombre = str(input(f"Ingrese el nombre del cliente {i+1} : "))
        lista_personas[i].append(nombre)
        
        identicacion = int(input(f"Ingrese la identificacion del cliente {i+1} : "))
        lista_personas[i].append(identicacion)
        
        edad = int(input(f"Ingrese la edad del cliente {i+1} : "))
        lista_personas[i].append(edad)
        
        dinero = float(input(f"Ingrese el dinero del cliente {i+1} : "))
        lista_personas[i].append(dinero)
        if contador >=0 and contador <= 15:
            lista_personas[i].append(f"A{(i+1)}")
        elif contador >15 and contador <= 30:
            lista_personas[i].append(f"B{(i+1)}")       
        elif contador >30 and contador <= 45:
            lista_personas[i].append(f"C{(i+1)}") 
        contador+=1   

def definir_pelicula():
    datos_pelicula.append([])
    titulo = str(input("Ingrese el titulo de la pelicula : "))
    datos_pelicula[0].append(titulo)

    genero = str(input("Ingrese el genero de la pelicula : "))
    datos_pelicula[0].append(genero)

    edad_minima = int(input("Ingrese la edad minima de la pelicula : "))
    datos_pelicula[0].append(edad_minima)

    tarifa = float(input("Ingrese la tarifa de la pelicula : "))
    datos_pelicula[0].append(tarifa)

titulo_personas=["Nombre","ID","Edad","Dinero","Posicion"]
titulo_pelicula =["Titulo","Genero","Edad Minima","Tarfia"]


lista_personas = [] 
datos_personas()
lista_personas = np.array(lista_personas)  
print(tabulate(lista_personas,headers=titulo_personas,tablefmt='fancy_grid'))
  
datos_pelicula = []
definir_pelicula()
datos_pelicula = np.array(datos_pelicula)
print(tabulate(datos_pelicula,headers=titulo_pelicula))