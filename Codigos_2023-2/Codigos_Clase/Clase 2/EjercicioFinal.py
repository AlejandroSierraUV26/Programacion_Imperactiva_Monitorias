
#*Entrada
nombre = str(input("Ingrese su nombre: "))

tipo_de_vehículo = int(input("Ingrese el tipo de vehiculo: "))
horas = int(input("Horas en el parqueadero: "))


#?Proceso
# Carro
if(tipo_de_vehículo == 1):
    precio = 5000
    if(horas>2):
        horas_Restantes = horas - 2
        precio = precio + (horas_Restantes * 3000)
# Moto
elif(tipo_de_vehículo == 2):
    precio = 3000
    if(horas>1):
        horas_Restantes = horas - 1
        precio = precio + (horas_Restantes * 2500)
elif(tipo_de_vehículo == 3):
    precio = 200_000
    if(horas>=24):
        horas_Restantes = horas - 24
        precio = precio + (horas_Restantes * 100_000)
else:
    print("Tipo de vehiculo no valido")
    
#!Salida
if(tipo_de_vehículo == 1 or tipo_de_vehículo == 2 or tipo_de_vehículo == 3):
    print(f"Recibo de Pago \n La Persona :{nombre} \n ocupo el servicio de parqueadero durante {horas} horas. \n Debe pagar {precio} \n Feliz dia.")

