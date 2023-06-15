# Creación de una lista de productos
productos = [
    {"nombre": "Leche", "precio": 2.50},
    {"nombre": "Pan", "precio": 1.50},
    {"nombre": "Huevos", "precio": 3.00},
    {"nombre": "Manzanas", "precio": 0.50},
    {"nombre": "Pasta de dientes", "precio": 2.00}
]

# Función para imprimir la lista de productos
def imprimir_productos():
    print("================================================")
    print("///////////////////Carrito//////////////////////")
    print("             Lista de productos:")
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto['nombre']} - ${producto['precio']}")
    print("================================================")

# Función para calcular el precio total de una compra
def calcular_total(productos_seleccionados):
    total = 0
    for producto in productos_seleccionados:
        total += producto["precio"]
    return total

# Función principal del programa
def main():
    # Imprimimos la lista de productos
    imprimir_productos()

    # Pedimos al usuario que seleccione los productos que desea comprar
    productos_seleccionados = []
    while True:
        print("Seleccione un producto \n(ingrese el número de producto) \no presione ENTER para finalizar la compra: ")
        print("================================================")
        seleccion = input("     Opcion : ")
        
        if seleccion == "":
            break
        try:
            seleccion = int(seleccion)
            if seleccion < 1 or seleccion > len(productos):
                raise ValueError()
            productos_seleccionados.append(productos[seleccion-1])
            print(f"Producto agregado: {productos[seleccion-1]['nombre']}")
        except ValueError:
            print("Seleccione un número válido")

    # Imprimimos la lista de productos seleccionados
    print("Productos seleccionados:")
    for i, producto in enumerate(productos_seleccionados):
        print(f"{i+1}. {producto['nombre']} - ${producto['precio']}")

    # Calculamos el precio total y lo imprimimos
    total = calcular_total(productos_seleccionados)
    print(f"Total de la compra: ${total}")

# Llamamos a la función principal
main()