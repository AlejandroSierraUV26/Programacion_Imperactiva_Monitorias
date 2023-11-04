def calcular_descuento(valor_compra):
    global tipo_cliente
    while(True):
        descuento = 0
        if tipo_cliente == "Regular":
            descuento = 0
            break
        elif tipo_cliente == "Frecuente":
            descuento = 0.1 * valor_compra
            break
        elif tipo_cliente == "VIP":
            descuento = 0.2 * valor_compra
            break
        else:
            print("Ingrese por favort un cliente valido")
            
            tipo_cliente = input("Ingrese el tipo de cliente: ")
    return descuento
            
if __name__ == "__main__":
    valor_compra = int(input("Ingrese el valor de compra : "))
    tipo_cliente = input("Ingrese el tipo de cliente: ")
    descuento = calcular_descuento(valor_compra)
    
    total_pagar = valor_compra - descuento
    
    print(f"""
          Resultados:
            - Precio total de la compra: ${valor_compra}
            - Tipo de cliente: Cliente {tipo_cliente}
            - Descuento: ${descuento}
            - Precio Total después del Descuento: ${total_pagar}
          """)
    