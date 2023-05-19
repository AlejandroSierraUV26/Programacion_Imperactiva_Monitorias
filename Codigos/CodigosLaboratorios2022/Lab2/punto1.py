"""
Autores: Alejandro Sierra Betancourt / Tina Maria Torres Tascon
Codigo Estudiante: 2259559-3743      / 2259729-3743
Fecha: 07/04/2022
Laboratorio 2
Descripcion: Fundamentos de programación. Punto 1 
"""
#Función calculoVenta
def calculo_venta(n_computadoras, precio_computadoras):
    precio_compra = n_computadoras * precio_computadoras
    if n_computadoras<5:
        descuento = precio_compra*0.1
    elif n_computadoras>=5 or n_computadoras<10:
        descuento = precio_compra*0.2
    elif n_computadoras>=10:
        descuento = precio_compra*0.4
    return descuento
for i in range(1, 4):
    print(f"Venta N° {i}")
#Recoleccion de variables por parte del usuario
    print("==========================================================================================")
    nombre_cliente = str(input("Ingrese su nombre: "))
    n_computadoras = int(input("¿Cuantas computadoras desea comprar?: "))
    precio_computadoras =float(input("Ingrese el precio unitario de las computadoras: $ ")) 
    precio_total = n_computadoras * precio_computadoras
    #Salida de los datos
    print("==========================================================================================")
    print(f"Precio de las computadoras   : ${precio_total} pesos\n Descuento obtenido . . . .   : ${calculo_venta(n_computadoras, precio_computadoras)} pesos\n Valor total a pagar : . . .  : ${precio_total - calculo_venta(n_computadoras, precio_computadoras)} pesos\n")
    print("==========================================================================================")