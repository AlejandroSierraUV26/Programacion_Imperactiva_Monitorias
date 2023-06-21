"""
Autor: Alejandro Sierra Betancourt 2259559-3743
Fecha: 16/03/2022
Descripcion: Fundamentos de programación. Punto 3 
"""

""""
Condominio Campestre

El condominio campestre “Nuevo Amanecer” tiene una serie de lotes para la venta y desea
implementar un programa que calcule el número de hectáreas de los lotes y el valor de venta
correspondiente. Los lotes son rectangulares y sus dimensiones están dadas en metros (ver Fig. 1).
Para el desarrollo del algoritmo debe solicitar las dimensiones 50del lote (su base y su altura) y el precio
por metro cuadrado del lote. Y debe mostrar el número de hectáreas, el valor del lote y el valor del
impuesto predial si se conoce que el porcentaje de este impuesto es del 1.3% sobre el valor del lote.


"""
print("Ingresar las siguientes dimenciones del lote en metros.")
#Recoleccion de variables por parte del usuario
altura_lote = float(input("Altura: "))
base_lote = float(input("Base: "))
precio_lote = float(input("Ahora, ingrese el precio por metro cuadrado del lote: "))
#Procesos empleados
numero_hectareas = (altura_lote * base_lote) / 10000
valor_lote = numero_hectareas * (precio_lote * 10000)
impuesto_predial =( 0.013 / valor_lote )
#Salida de los datos
print(f"Segun los datos ingresados, el lote tiene {numero_hectareas} Hectareas cuadradas con un precio de ${valor_lote}, el valor del impuesto predial es ${impuesto_predial} ")