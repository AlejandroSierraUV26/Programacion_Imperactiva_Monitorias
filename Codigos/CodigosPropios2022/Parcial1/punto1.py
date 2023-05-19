"""
Autor: Alejandro Sierra Betancourt
Fecha: 8 de Abril 2022
Descripcion: Registro tienda
"""
def pago(tipo_trabajador, horas_trabajadas,tiempo_empresa):
    if horas_trabajadas>=192:
        horas_extra = horas_trabajadas-192
        bonificacion = 0
        if horas_trabajadas>=193:
            if tiempo_empresa >=5:
                    bonificacion = 1.2
            if tipo_trabajador == 1:
                salario_hora = 3000000/192
                pago = 3000000 + 1.2*horas_extra *salario_hora
            if tipo_trabajador == 2:
                salario_hora = 2000000/192
                pago = 2000000 + 1.2*horas_extra *salario_hora
            if tipo_trabajador == 3:
                salario_hora = 1500000/192
                pago = 1500000 + 1.2*horas_extra *salario_hora
            return(pago * bonificacion)
        else: return("Por favor cumpla con la normativa de trabajar mas de 192 horas ")

print("Opcion 1: Ejecutivo \nOpcion 2: Administrativo \nOpcion 3: Auxiliar")
tipo_trabajador = int(input("Seleccione la opcion correspondiente: "))
horas_trabajadas = float(input("Ingrese el numero total de horas trabajadas: "))
tiempo_empresa = int(input("Ingrese los años que lleva en la empresa: "))
print(f"Su salario final es : {pago(tipo_trabajador, horas_trabajadas,tiempo_empresa)}")