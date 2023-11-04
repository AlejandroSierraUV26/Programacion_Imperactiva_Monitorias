def municipio(nombre_municipio):
    i = 0
    total_productos = 0
    mayor = 0
    punto = 0

    while(i<5):    
        cantidad_productos = int(input("Cantidad productos  : "))
        total_productos += cantidad_productos
        if cantidad_productos > mayor : 
            mayor = cantidad_productos
            punto = i+1
        i+=1
    print(f"El punto de entrega con mayor pedido en el municipio {nombre_municipio} es el punto {punto} con un pedido de {mayor} productos.")
    return total_productos

if __name__ == "__main__":
    municipio1 = input("Ingrese el nombre del primer municipio: ")
    total_municipio1 = municipio(municipio1)

    municipio2 = input("Ingrese el nombre del segundo municipio: ")
    total_municipio2 = municipio(municipio2)

    municipio3 = input("Ingrese el nombre del tercer municipio: ")
    total_municipio3 = municipio(municipio3)
    
    print(f"Total de productos pedidos en {municipio1}: {total_municipio1}")
    print(f"Total de productos pedidos en {municipio2}: {total_municipio2}")
    print(f"Total de productos pedidos en {municipio3}: {total_municipio3}")
    
    
    

