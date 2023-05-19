"""
Autor: Alejandro Sierra Betancourt
Fecha: 8 de Abril 2022
Descripcion: Registro tienda
"""
from functools import total_ordering


total_consumo = float(input("Ingrese el consumo total de energia: "))
if total_consumo >300:
    total = 300*50
    consumo = total_consumo -300
    if consumo >200:
        if consumo <200:
            total = consumo * 100
        else: 
            consumo = consumo -200
            total = total + 200 * 100
    if consumo >500:
        if consumo <500:
            total = consumo * 150
        else: 
            consumo = consumo -500
            total = total + 500 * 150
    if consumo >0:
            total = total + consumo * 200
    print(total)
    