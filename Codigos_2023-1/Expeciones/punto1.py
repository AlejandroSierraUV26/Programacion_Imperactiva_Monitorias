"""
Autor: Alejandro Sierra Betancourt 2259559-3743
Fecha: 16/03/2022
Descripcion: Fundamentos de programación. Punto 3 
"""

""""
Suramericano sub 20
La FIFA de Colombia requiere de un programa que permita calcular la tabla de resultados de
los equipos que están participando en el Suramericano sub 20. Los resultados por equipo se
expresan en función de la información que se presenta en la Tabla 1 (Ejemplo puntuación de
Colombia).
Usted debe desarrollar un algoritmo que calcule los puntos obtenidos por el equipo y la
diferencia de goles. Tenga en cuenta que por cada partido ganado obtendrá 3 puntos, por
cada partido empatado 1 punto y por cada partido perdido 0 puntos.
"""
#?Recoleccion de variables por parte del usuario
while(True):
    print("")
    try:
        nombre_equipo = str(input("Ingrese el nombre del equipo: "))
        partidos_ganados = int(input("Ingrese el numero de partidos ganados: "))
        partidos_empatados = int(input("Ingrese el numero de partidos empatados: "))
        partidos_perdidos = int(input("Ingrese el numero de partidos perdidos: "))
        goles_favor = int(input("Ingrese el numero de goles a favor: "))
        goles_contra = int(input("Ingrese el numero de goles en contra: "))
        break
    except ValueError:
        print("Valor incorrecto intente nuevamente")
    
#*Codigo continua...

#?Procesos empleados
total_puntos = (partidos_ganados * 3) + (partidos_empatados * 1)
total_partidos = (partidos_ganados + partidos_empatados + partidos_perdidos)
diferencia_goles = goles_favor - goles_contra
#?Salida de los datos
print(f"Nombre equipo: {nombre_equipo}: Pts: {total_puntos}, PJ: {total_partidos}, G:{partidos_ganados}, E:{partidos_empatados}, P:{partidos_perdidos}, GF: {goles_favor}, GC: {goles_contra}, Dif: {diferencia_goles}")