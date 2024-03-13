# """
# Realizar una conversion exacta de las horas, minutos y segundos. 

# El valor exacto para los segundos no deben exceder de los 60 segundos.

# El valor exacto para los minutos no deben exceder de los 60 minutos.

# El valor exacto para las horas no deben exceder de las 24 horas.

# Ejemplo: 

# Entrada: 1 hora 120 minutos 120 segundos

# Salida: 03:02:00

# Ejemplo: 

# Entrada: 16 horas 300 minutos 10002 segundos

# Salida: 23:46:42
# """



# minutos = 300
# segundos = 128

# minutos = minutos + segundos // 60

# segundos = segundos % 60

# print(f"{minutos:02d} : {segundos:02d}")


"""
Autor: Alejandro Sierra
Fecha: 13/03/2024

Tema: Ejercicio Monitorias



"""

import math

cantidad_almacenamiento = float(input("Ingrese la cantidad a almacenar : "))

precio_discos = float(input("Ingrese el precio de los discos: "))

# 1GB -> 1024 MB

#? 1 Disco -> 700MB


unidad_en_mb = cantidad_almacenamiento * 1024

cantidad_discos = unidad_en_mb / 700

cantidad_discos = math.ceil(cantidad_discos)

valor_neto = cantidad_discos * precio_discos

valor_total = valor_neto * 1.19


print(f"Para almacenar {cantidad_almacenamiento} GB en {cantidad_discos} se necesitan ${valor_total}")





