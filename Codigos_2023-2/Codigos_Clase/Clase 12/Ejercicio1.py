def calcular_interes(valor,duracion):
    valor_interes = 0
    if valor < 2_000_000 and valor > 0 and duracion <= 12 and duracion >= 1:
        valor_interes = valor * 0.035
    elif valor >= 2_000_000 and valor <= 6_000_000 and duracion >= 12 and duracion <= 24:
        valor_interes = valor * 0.03
    elif valor > 6_000_000 and valor <= 10_000_000 and duracion >= 24 and duracion <= 36:
        valor_interes = valor * 0.023
    elif valor > 10_000_000 and duracion >= 60:
        valor_interes = valor * 0.01
    else:
        valor_interes =  valor * 0.018
    return valor_interes

def valor_couta(valor,duracion,credito):
    return (valor + credito) / duracion

def pago_total(valor_mes,duracion):
    return valor_mes * duracion

if __name__ == '__main__':
    valor = int(input("Ingrese el valor del prestamo : "))
    duracion = int(input("Ingrese la duracion del prestamo : "))
    interes = calcular_interes(valor,duracion)
    valor_mes = valor_couta(valor,duracion,interes)
    total_pago = pago_total(valor_mes,duracion)
    print(f"""
          
          Datos del Asociado:
            - Valor del crédito solicitado: ${valor}
            - Período en meses: {duracion}

            Valores Calculados:
            - Interés Mensual: ${interes}
            - Cuota Mensual: ${valor_mes} (aproximadamente)
            - Valor Total a Pagar: ${total_pago} (aproximadamente)
          
          """)
    



