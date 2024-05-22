import random
import datetime

datos = []
fechas_junio = [5,6,12,13,19,20,26,27]

vuelos_usados = set()

for i in range(0,100):        
        ciudades = ["Cali", "Bogota", "Santa Marta", "Medellin", "Cartagena"]

        abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        vuelo = str(random.choice(abecedario)) + str(random.randint(100, 999))
        while vuelo in vuelos_usados:
            vuelo = str(random.choice(abecedario)) + str(random.randint(100, 999))

        vuelos_usados.add(vuelo)
        fecha = "2024-06-" + str(random.choice(fechas_junio))
        año = int(fecha[0:4])
        mes = int(fecha[5:7])
        dia = int(fecha[8:10])
        
        hora_salida = datetime.datetime(año,mes,dia, random.randint(0, 23), random.randint(0, 59))
        hora_salida = hora_salida.strftime("%H:%M:%S")
        
        while True:
            hora_llegada = datetime.datetime(año,mes,dia, random.randint(0, 23), random.randint(0, 59))
            hora_llegada = hora_llegada.strftime("%H:%M:%S")
            diferencia = hora_llegada - hora_salida
            diferencia = diferencia.total_seconds()
            if diferencia > 0 and diferencia < 18000:
                break
            
        

        valor_min = random.randint(100000, 500000)
        valor_medio = random.randint(500000, 1000000)
        valor_max = random.randint(1000000, 5000000)
        
        ciudad_origen = random.choice(ciudades) 
        ciudades.remove(ciudad_origen)
        ciudad_destino = random.choice(ciudades)
        
        datos.append([vuelo, fecha, hora_salida, hora_llegada, valor_min, valor_medio, valor_max, ciudad_origen, ciudad_destino])
        
print("# Vuelo, Fecha, Hora Salida, Hora Llegada, Valor Min, Valor Medio, Valor Max, Ciudad Origen, Ciudad Destino")
for i in datos:
    print(i)






                    