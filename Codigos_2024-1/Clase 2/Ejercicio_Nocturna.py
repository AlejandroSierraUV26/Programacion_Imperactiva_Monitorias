# import math
# # Entrada de datos

# nombre = input("Ingrese su nombre : ")

# cantidad_almacenamiento = float(input("Ingrese el valor a almacenar : "))

# precio_unitario_cd = float(input("Ingrese el valor unitario de los CD's : "))

# #? Proceso

# cantidad_almacenamiento_mb = cantidad_almacenamiento * 1024

# cantidad_cds = cantidad_almacenamiento_mb / 700

# cantidad_cds = round(cantidad_cds,0)

# print(cantidad_cds)

# cantidad_cds = math.ceil(cantidad_cds)

# valor_neto = cantidad_cds * precio_unitario_cd

# iva = 0.19

# valor_total = valor_neto + (valor_neto * iva)
# valor_total = valor_neto * (1+iva)
# #! Salida
# print(f"Para almacenar {cantidad_almacenamiento} GB se necesitan {cantidad_cds} \n que valen ${valor_total}")



"""
En un almacen de relojes, se descontrolaron las horas.
Su tarea es representar cada hora como se debe en sus limites establecidos

Segundos [0;60) 
Minutos  [0;60)
Horas [0:24]

Ejemplo: 

Segundos 345
Minutos 234
Horas 0

Solucion: 
Horas :3
Minutos :59
Segundos :45

 
"""

minutos = 59
segundos = 59
horas = 1

minutos = minutos + segundos // 60
segundos = segundos % 60
horas = horas + minutos // 60
minutos = minutos % 60

print(f"Horas :{horas}")
print(f"Minutos :{minutos}")
print(f"Segundos :{segundos}")

# segundos = 345
# minutos = 234
# horas= 0

# minutos = minutos + segundos // 60
# segundos = segundos % 60
# horas = horas + minutos // 60

# minutos = minutos % 60

# print(f"Horas :{horas}")
# print(f"Minutos :{minutos}")
# print(f"Segundos :{segundos}")


