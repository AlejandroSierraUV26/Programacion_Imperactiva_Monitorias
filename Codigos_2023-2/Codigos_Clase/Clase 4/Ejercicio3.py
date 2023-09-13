""""
Cálculo de número de CDs

Los profesores de la Universidad del Valle desean conocer la cantidad de CDs 
que necesitan comprar para hacer una copia de seguridad 
del disco duro de sus computadores.
Lo han contratado a usted para que realice un algoritmo que calcule la cantidad 
de los CDs requeridos y el precio más IVA de estos. 
Para ello debe solicitar el nombre del profesor, la capacidad
de almacenamiento del disco duro en GB y el valor unitario del CD. 
Una vez se han calculado los valores se debe visualizar los resultados obtenidos.
Tenga en cuenta que el disco duro está lleno y que su 
capacidad está dada en GigaBytes (GB).
Además, un CD en blanco tiene una capacidad 
de 700 MegaBytes (MB) y que un GB equivale a 1,024 MB.

Entradas: 

nombre: str // Nombre del profesor
capacidad: float // Capacidad del disco duro en GB
valor: float // Valor unitario del CD
iva = 19/100 

Proceso: 

capacidad = capacidad * 1024

cd = capacidad / 700

precio = cd * precio + (iva * precio)


Salidas:

print(f"El total de CD son: {cd} y debe pagar {precio}")

"""
import math

nombre = str(input("Nombre :"))
capacidad = float(input("Capacidad :"))
valor = float(input("Valor: "))

iva = 19/100

capacidad = capacidad * 1024
cd = capacidad / 700

cd = math.ceil(cd)

valor = (valor * cd )+ (iva*valor)

print(f"la cantidad de disco que puede comprar es : {cd} con precio de {valor}")
