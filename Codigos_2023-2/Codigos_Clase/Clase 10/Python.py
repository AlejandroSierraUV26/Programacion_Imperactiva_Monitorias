def calcular_precio(n_adultos,n_niños):
    obtener_dia = False
    total_pagar = (n_adultos * 16_000) + (n_niños * 10_000)
    if n_adultos>=3 and n_niños >=2:
        total_pagar = (total_pagar*0.8)
        obtener_dia = True
    return total_pagar,obtener_dia
    

if __name__ == "__main__":
    n_adultos = int(input("Ingrese el número de adultos: "))

    n_niños = int(input("Ingrese el número de niños: "))

    total_pagar, obtener_dia = calcular_precio(n_adultos,n_niños)

    print("Total pagar  : ", total_pagar)
    if obtener_dia: 
        print("Tiene el descuento")
    else:
        print("NO obtuvo el descueto")
        
    