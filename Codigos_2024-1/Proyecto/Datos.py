import random
import datetime

datos = []
fechas_junio = [5,6,12,13,19,20,26,27]

vuelos_usados = set()

for i in range(0,100):        
        ciudades = ["Cali", "Bogota", "Santa Marta", "Medellin", "Cartagena", "Barranquilla", "Manizales", "Pereira","San Andres"]

        abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        vuelo = str(random.choice(abecedario)) + str(random.randint(100, 999))
        while vuelo in vuelos_usados:
            vuelo = str(random.choice(abecedario)) + str(random.randint(100, 999))

        vuelos_usados.add(vuelo)
        fecha = "2024-06-" + str(random.choice(fechas_junio))

        hora = datetime.datetime(2024, 6, random.choice(fechas_junio), random.randint(0, 23), random.randint(0, 59))
        hora = hora.strftime("%H:%M:%S")

        valor_min = random.randint(100000, 500000)
        valor_medio = random.randint(500000, 1000000)
        valor_max = random.randint(1000000, 5000000)
        
        ciudad_origen = random.choice(ciudades) 
        ciudades.remove(ciudad_origen)
        ciudad_destino = random.choice(ciudades)
        
        datos.append([vuelo, fecha, hora, valor_min, valor_medio, valor_max, ciudad_origen, ciudad_destino])
        
for i in datos:
    print(i)






                    