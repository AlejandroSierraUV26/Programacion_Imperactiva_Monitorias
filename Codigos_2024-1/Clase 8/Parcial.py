
def calcular_pedidos():
    mayor = 0
    punto_venta = 0
    total = 0
    for punto in range(5):
        pedidos = int(input(f"Ingrese el total de pedidos para el punto {punto+1} : "))
        total+=pedidos
        if pedidos > mayor:
            mayor = pedidos
            punto_venta = punto+1
        
    return mayor, punto_venta, total
 
if __name__ == "__main__":
    mensaje_final = ""
    for i in range(3):
        nombre_municipio = input("Ingrese el nombre del municipio : ")
        mayor, punto, total_productos = calcular_pedidos()
        mensaje_final += f"El punto que más vendio fue {punto} con un total de {mayor} \n Total Productos {total_productos} \n"
        
        
    print(mensaje_final)
    
    
    