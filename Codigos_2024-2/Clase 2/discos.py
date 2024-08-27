"""
 Los profesores de la Universidad del Valle desean conocer la cantidad de CDs que necesitan 
 comprar para hacer una copia de seguridad del disco duro de sus computadores.
 Lo han contratado a usted para que realice un algoritmo que calcule la cantidad de los CDs
 requeridos y el precio más IVA de estos. Para ello debe solicitar el nombre del profesor, la capacidad
 de almacenamiento del disco duro en GB y el valor unitario del CD. Una vez se han calculado los
 valores se debe visualizar los resultados obtenidos.
 Tenga en cuenta que el disco duro está lleno y que su capacidad está dada en GigaBytes (GB).
 
 
 
 
 
 Además, un CD en blanco tiene una capacidad de 700 MegaBytes (MB) y que un GB equivale a
 1,024 MB.
 Ejemplo:
 Tamaño del disco: 40GB
 Valor del CD: 5000
 Proceso: Total a almacenar: 40.960
 Número de CD: 58,51 CD, aplicando techo son 59.
 La salida debería ser así:
 “Para almacenar 40GB se requieren 59 Cds que cuesta $295.000”
 
"""
import math 
# Entrada de datos

nombre_profesor = str(input("Ingrese el nombre del profesor: "))

capacidad_disco = float(input("Ingrese la cantidad a almacenar : "))

valor_disco = float(input("Ingrese el valor del disco : "))


# *Proceso

cantidad_mb = capacidad_disco * 1024

cantidad_discos = cantidad_mb / 700

total_discos = math.ceil(cantidad_discos) 

valor_total = total_discos * valor_disco



# !Salida

print(f"El profesor {nombre_profesor} requiere almacenar {capacidad_disco} GB")

print(f"Serian un total {total_discos} por un valor de $ {valor_total}")












