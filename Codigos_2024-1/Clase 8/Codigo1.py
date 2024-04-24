"""
Para atender la demanda del consumo de gaseosa la sabrosura la empresa tiene como clientes 3 municipios
cercanos a la ciudad de Cali, donde se tiene la bodega principal, y desde la cual son despachados los
productos, el encargado de programar las entregas necesita saber cuál de los puntos de entrega de cada
municipio ha hecho el mayor pedido con el fin de atenderlo con prioridad en la programación de la próxima
entrega. Cada municipio cuenta con cinco (5) puntos de entrega. Se pide elaborar un programa que lea el
nombre de cada municipio y la cantidad de productos pedidos en cada punto de entrega. El programa debe
determine cuál punto de entrega en cada municipio ha hecho el mayor pedido y el total de productos
solicitados por municipio.
• Elabore una función que reciba el nombre del municipio, la función debe pedir la cantidad de
productos pedidos para cada punto de entrega en el municipio y calcular e imprimir el punto de
entrega con mayor pedido.
• Elabore una función que imprima el nombre del municipio y el total de productos pedidos
Nota: Utilice solo ciclos mientras que (while) para su solución


"""

def mayor_pedido(municipio):
    mayor = 0
    punto = 0
    i = 1
    while i <= 5:
        pedido = int(input(f'Ingrese la cantidad de productos pedidos en el punto de entrega {i}: '))
        if pedido > mayor:
            mayor = pedido
            punto = i
        i += 1
    print(f'El punto de entrega con mayor pedido en el municipio {municipio} es el punto {punto} con {mayor} productos')
    
def total_productos(municipio):
    total = 0
    i = 1
    while i <= 5:
        pedido = int(input(f'Ingrese la cantidad de productos pedidos en el punto de entrega {i}: '))
        total += pedido
        i += 1
    print(f'El total de productos pedidos en el municipio {municipio} es: {total}')
    
municipio1 = input('Ingrese el nombre del primer municipio: ')
mayor_pedido(municipio1)
total_productos(municipio1)

municipio2 = input('Ingrese el nombre del segundo municipio: ')
mayor_pedido(municipio2)
total_productos(municipio2)

municipio3 = input('Ingrese el nombre del tercer municipio: ')
mayor_pedido(municipio3)
total_productos(municipio3)

