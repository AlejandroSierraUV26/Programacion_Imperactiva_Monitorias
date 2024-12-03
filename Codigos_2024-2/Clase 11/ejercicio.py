import numpy as np
from tabulate import tabulate
"""
Se le contrata para realizar una aplicacion para el regristro de un parqueadero

El parqueadero tiene un cupo de 10 vehiculos

Servicios:
Diario : Carro -> $5.000, Moto -> $2.000
Semanal: Carro -> $25.000, Moto -> $10.000
Mensual: Carro -> $80.000, Moto -> $30.000

El parqueadero debe tener las siguientes funcionalidades:
1. Ingresar un vehiculo
2. Retirar un vehiculo
3. Mostrar el estado actual del parqueadero
4. Mostrar las ganancias del dia
5. Mostrar las ganancias del mes
6. Mostrar las ganancias del año
7. Salir



"""
def menu():
    print("""
    1. Ingresar un vehiculo
    2. Retirar un vehiculo
    3. Mostrar el estado actual del parqueadero
    4. Mostrar las ganancias del dia
    5. Mostrar las ganancias del mes
    6. Mostrar las ganancias del año
    7. Salir  
          
          
          
          """)
    return int(input(": "))


def ingresar_vehiculo():
    nombre_propietario = input("Ingrese el nombre del propietario: ")
    nombre_vehiculo = input("Ingrese el nombre del vehiculo: ")
    modelo = input("Ingrese el modelo del vehiculo: ")
    placa = input("Ingrese la placa del vehiculo: ")
    tipo_vehiculo = input("Ingrese el tipo de vehiculo (Carro/Moto): ")
    tipo_servicio = input("Ingrese el tipo de servicio (Diario/Semanal/Mensual/PRESIONAR ENTER SI SOLO QUIERE INGRESARLO): ")
    color = input("Ingrese el color del vehiculo: ")
    valor_sentimental = float(input("Ingrese el valor sentimental del vehiculo: "))
    
    return [nombre_vehiculo, modelo, color, valor_sentimental, tipo_vehiculo, placa, nombre_propietario,tipo_servicio]
    
    
def ingresar_datos(datos):
    with open(fr"Clase 11\parqueadero.txt", "a") as archivo:
        mensaje = datos[0]
        
        for elem in datos[1:]:
            mensaje = mensaje + ", " + str(elem)
            
        archivo.write(mensaje + "\n")
    print("Datos guardados correctamente")
    

def retirar_vehiculo():
    placa = input("Ingrese la placa del vehiculo a retirar: ")
    datos = leer_datos()
    encontrado = False
    
    for i in range(len(datos)):
        if datos[i][5] == placa:
            datos = np.delete(datos, i, 0)
            encontrado = True
            break
    
    if encontrado:
        with open(fr"Clase 11\parqueadero.txt", "w") as archivo:
            for vehiculo in datos:
                mensaje = ", ".join(map(str, vehiculo)) # Revisar
                archivo.write(mensaje + "\n")
        print("Vehiculo retirado correctamente")
    else:
        print("Vehiculo no encontrado")
    

def mostrar_parqueadero():
    datos = leer_datos()
    print(tabulate(datos, headers=["Nombre", "Modelo", "Color", "Valor sentimental", "Tipo vehiculo", "Placa", "Nombre propietario", "Tipo servicio"], tablefmt="fancy_grid", floatfmt=(".0f")))
    
    

def ganancias_dia():
    print("Funcion ganancias")
    pass

def ganancias_mes():
    print("Funcion ganancias")
    pass

def ganancias_año():
    print("Funcion ganancias")
    pass
def leer_datos():
    try:
        with open(fr"Clase 11\parqueadero.txt", "r") as archivo:
            datos = archivo.read()
            datos = datos.split("\n")
            # Quitar los espacios en blanco
            datos = [elem.replace(" ", "").split(",") for elem in datos if elem]
            
            for i in range(len(datos)):
                datos[i][3] = float(datos[i][3])
                
            datos = np.array(datos)
            return datos
    except FileNotFoundError:
        return []


    
while True: 
    opcion = menu()
    if opcion == 1:
        vehiculo = ingresar_vehiculo()
        ingresar_datos(vehiculo)
    elif opcion == 2:
        retirar_vehiculo()
    elif opcion == 3:
        mostrar_parqueadero()
    elif opcion == 4:
        ganancias_dia()
    elif opcion == 5:
        ganancias_mes()
    elif opcion == 6:
        ganancias_año()
    elif opcion == 7:
        break
    else:
        print("Opcion incorrecta")
        continue