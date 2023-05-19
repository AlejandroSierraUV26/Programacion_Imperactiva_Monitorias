"""
Autor: Alejandro Sierra Betancourt 2259559-3743
Fecha: 16/03/2022
Descripcion: Fundamentos de programación. Punto 3 
"""

""""
Cálculo de número de CDs

Los profesores de la Universidad del Valle desean conocer la cantidad de CDs que necesitan comprar
para hacer una copia de seguridad del disco duro de sus computadores.
Lo han contratado a usted para que realice un algoritmo que calcule la cantidad de los CDs
requeridos y el precio más IVA de estos. Para ello debe solicitar el nombre del profesor, la capacidad
de almacenamiento del disco duro en GB y el valor unitario del CD. Una vez se han calculado los
valores se debe visualizar los resultados obtenidos.
Tenga en cuenta que el disco duro está lleno y que su capacidad está dada en GigaBytes (GB).
Además, un CD en blanco tiene una capacidad de 700 MegaBytes (MB) y que un GB equivale a
1,024 MB.

"""
#Se importa math para utilizar techo
import math
#Recoleccion de variables por parte del usuario
nombre_docente = str(input("Ingrese su nombre: "))
cantidad_almacenamiento = float(input("Ingrese la cantidad de almacenamiento en GB: "))
valor_CD = float(input("Ingrese el precio de cada CD: "))
#Procesos empleados
total_almacenar = cantidad_almacenamiento * 1024
total_CD = math.ceil(total_almacenar/700)
precio_CD = valor_CD * total_CD
#Salida de los datos
print(f"Para almacenar {cantidad_almacenamiento} GB se requiere {total_CD} con un precio de ${precio_CD}")