def calculo(base,exponente):
    resultado = 1
    for i in range(0,exponente):
        resultado *= base
    return resultado

def calculo2(base,exponente):
    resultado = 1
    i = 0
    while i < exponente:
        resultado *= base
        i+=1
    return resultado


def funcion(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * funcion(base,exponente-1)
    

if __name__ == '__main__':
    base = int(input("Ingrese la base : "))
    exponente = int(input("Ingrese el exponente : "))
    
    print(calculo(base, exponente))
    print(calculo2(base, exponente))
    print(funcion(base, exponente))