def potencia1(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia1(base,exponente-1)

def potencia2(base,exponente):
    resultado = 1
    for i in range(0,exponente):
        resultado *= base
    return resultado 


if __name__ == "__main__":
    base = int(input("Ingrese la base : "))
    exponente = int(input("Ingrese el exponente : "))
    print("Por recursividad ", potencia1(base,exponente))
    print("Por bucle for : ", potencia2(base,exponente))