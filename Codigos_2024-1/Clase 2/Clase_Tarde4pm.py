import math

print("Hola bienvendio a la calculadora de discos")

can_almacenamiento = float(input("Ingrese el tamaño del disco : "))

precio_cd = 5000

disco = 700 #?mb

can_almacenamiento = can_almacenamiento * 1024

cantidad_cds = can_almacenamiento / disco


#? Aplicar ley techo
cantidad_cds = math.ceil(cantidad_cds)

precio_neto = cantidad_cds * precio_cd

precio_total = precio_neto * 1.19

print(f"La cantidad de discos que se necesitan son {cantidad_cds} \nSe necesitan ${precio_total} para almacenar {can_almacenamiento /1024}")
