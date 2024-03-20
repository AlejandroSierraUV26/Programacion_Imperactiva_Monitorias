# print("Hola Mundo")

# nombre = "Juan"

# print(type(nombre))

# numero = int(10)
# numero_decimal = float(10.5)

# condicion = bool(0)

# nombre = input("Ingrese su nombre: ")

# edad = int(input("Ingrese su edad: "))

# print(f"Su nombre es {nombre} y su edad es {edad}")
# print("Su nombre es ", nombre , " y su edad es ", edad)

# """

# +  -> Suma
# -  -> Resta
# /  ->Division
# / /  ->Division exacta
# *  -> Multiplicacion
# ** ->Potenciacion

# % -> Modulo


# """



# # if condicion : 
# #     print("Es verdadero")
# # elif condicion : 
# #     print("Es verdadero")
# # else:
# #     print("Es falso")

# match nombre:
#     case "Juan":
#         print("Hola Juan")
#     case "Pedro":
#         print("Hola Pedro")
#     case "Maria":
#         print("Hola Maria")






"""
Autor: Alejandro Sierra
Fecha: 13/03/2024


"""
print("Bienvenido a la FIFA COLOMBIA SUB-20")

#! Entrada de datos
nombre_equipo = input("Ingrese el nombre del equipo : ")

partidos_jugados = int(input("Ingrese los partidos jugados : "))

partidos_ganados = int(input("Ingrese los partidos ganados : ")) 

partidos_empatados = int(input("Ingrese los partidos empatados : ")) 

partidos_perdidos = int(input("Ingrese los partidos perdidos : ")) 

goles_favor = int(input("Ingrese los goles a favor : "))

goles_contra = int(input("Ingrese los goles en contra :"))

diferencia_goles = goles_contra - goles_favor



#? Salida

print(f"""
      
      Nombre Equipo : {nombre_equipo} 
        Partidos Jugados: {partidos_jugados}
        Partidos Ganados: {partidos_ganados}
        Partidos Empatados: {partidos_empatados}
        Partidos Perdidos: {partidos_perdidos}
        Goles a Favor: {goles_favor}
        Goles en Contra: {goles_contra}
        Diferencia de Goles: {diferencia_goles}
        
        
        Puntos : {partidos_ganados * 3 + partidos_empatados * 1 + partidos_perdidos * 0}
        
        """)
      

