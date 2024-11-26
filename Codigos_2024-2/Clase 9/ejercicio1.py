def mayor_pedido(municipio):
    mayor = 0
    punto = 0
    for i in range(1,6):
        pedido = int(input(f"Digite la cantidad de productos pedidos en el punto de entrega {i}: "))
        if pedido > mayor:
            mayor = pedido
            punto = i
    print(f"El punto de entrega con mayor pedido en el municipio {municipio} es el punto {punto}")
    return mayor

def total_productos(municipio):
    total = 0
    for i in range(1,6):
        pedido = int(input(f"Digite la cantidad de productos pedidos en el punto de entrega {i}: "))
        total += pedido
    print(f"El total de productos pedidos en el municipio {municipio} es de {total}")
    return total

municipio1 = input("Digite el nombre del municipio 1: ")
municipio2 = input("Digite el nombre del municipio 2: ")
municipio3 = input("Digite el nombre del municipio 3: ")

total1 = total_productos(municipio1)
total2 = total_productos(municipio2)
total3 = total_productos(municipio3)

mayor1 = mayor_pedido(municipio1)
mayor2 = mayor_pedido(municipio2)
mayor3 = mayor_pedido(municipio3)

if total1 > total2 and total1 > total3:
    print(f"El municipio con mayor pedido es {municipio1} con un total de {total1} productos")
elif total2 > total1 and total2 > total3:
    print(f"El municipio con mayor pedido es {municipio2} con un total de {total2} productos")
else:
    print(f"El municipio con mayor pedido es {municipio3} con un total de {total3} productos")
    
if mayor1 > mayor2 and mayor1 > mayor3:
    print(f"El punto de entrega con mayor pedido en el municipio {municipio1} es el punto {mayor1}")
elif mayor2 > mayor1 and mayor2 > mayor3:
    print(f"El punto de entrega con mayor pedido en el municipio {municipio2} es el punto {mayor2}")
else:
    print(f"El punto de entrega con mayor pedido en el municipio {municipio3} es el punto {mayor3}")

