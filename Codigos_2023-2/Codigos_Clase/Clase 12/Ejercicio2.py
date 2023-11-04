def calcular_impuesto(valor,ciudad):
    impuesto = 0
    if ciudad == "Cali":
        impuesto = 0.08 * valor
    elif ciudad == "Bogota":
        impuesto = 0.09 * valor
    elif ciudad == "Tulua":
        impuesto == 0.06 * valor
    else:
        print(f"La ciudad {ciudad} no esta en la tabla, se le aplicara como 5 % de impuestos")
        impuesto == 0.05 * valor
    return impuesto
    
    
if __name__ == "__main__":
    while(True):
        valor = int(input("Ingrese la cantidad del producto : "))
        ciudad = input(" Cali \n Bogota \n Tulua\n Ingrese a la ciudad de compra : ")
        
        impuesto = calcular_impuesto(valor,ciudad)
        
        total_pagar = impuesto + valor
        
        print(f"""
              
              Resultados:
                - Precio del artículo: ${valor}
                - Estado: {ciudad}
                - Impuesto: ${impuesto}
                - Precio Total: ${total_pagar}
              """)    
        opcion = input("Desea calcular otro producto (Y/N) : ")
        if opcion == "N":
            break