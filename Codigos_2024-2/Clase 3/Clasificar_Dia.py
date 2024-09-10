# dia = str(input("Ingrese el dia de hoy: (Lunes, Martes, Miercoles, ...)"))

# if dia == "Lunes":
#     print("Feliz Lunes")
# elif dia == "Martes":
#     print("Feliz Martes")
# elif dia == "Miercoles":
#     print("Feliz Miercoles")
# elif dia == "Jueves":
#     print("Feliz Jueves")
# elif dia == "Viernes":
#     print("Feliz Viernes")
# elif dia == "Sabado":
#     print("Feliz Sabado")
# elif dia == "Domingo":
#     print("Feliz Domingo")
# else:
#     print("Dia no valido")
    



# print("Pregunta de programacion en ABCD")


# print("Pregunta : ")
# print("¿Cual es el lenguaje de programacion mas popular?")
# print("A) Python")
# print("B) Java")
# print("C) C++")
# print("D) JavaScript")

# # 4 Preguntas con 4 opciones 









# print("""
#       =========================================================
#       Bienvenido a quien quiere ser millonario  
      
#       Si atina todas las respuestas ganara 1 millon de dolares
      
#       =========================================================
      
      
#       """)


# # ?input("Mensaje a mostrar en pantalla y recibir respuesta del usuario")
# # ?print("Mensaje a mostrar en pantalla")
# # ?if condicion : 
# #    print("Mensaje a mostrar en pantalla") # *Si la condicion es verdadera
# # ?elif condicion:
# #   print("Mensaje a mostrar en pantalla") # ?Si la condicion inicial es falsa, evalua otra condicion
# # ?else:
# #    print("Mensaje a mostrar en pantalla") # !Si la condicion es falsa



# import time

# print(1)
# time.sleep(2)
# print(2)
# time.sleep(2)
# print(3)
# time.sleep(2)
# print(4)
# time.sleep(2)
# print(5)
# time.sleep(2)










# nombre = "Alejandro".upper()
# print(nombre)
# nombre_2 = "ALEJANDRo".upper()
# print(nombre_2)


# print(nombre == nombre_2)

























import time
print("""
      BIENVENIDO A QUIEN QUIERE SER MILLONARIO
      
      RESPONDA TODAS LAS RESPUESTAS Y GANARA 
      1 MILLON DE PESOS
      
      
      
      """)  


premio = 0

pregunta1 = "¿Como se llama el Monitor?"
pregunta2 = "¿Cual es el rio más del mundo?"
pregunta3 = "¿Cual es el pais con más habitantes del mundo?"

repuestas_letras = ("A","B","C","D")

respuesta1 = ("A. Pancho Villa", "B. Carlos", "C. Alejandro", "D. No sé")
respuesta2 = ("A. Nilo", "B. Missipi", "C. Cauca", "D. Amazonas")
respuesta3 = ("A. Tuluá", "B. China", "C. Barrancamermeja", "D. India")


# Pregunta 1

print("Responda la pregunta y ganara $333.333")

time.sleep(1)

print(pregunta1)
print(respuesta1)

opcion = str(input("Ingrese la opcion correcta : "))
if opcion == repuestas_letras[2]:
    premio += 333_333
    print("Gano la primera pregunta!!!!!!")
else:
    print("Perdio el juego")
    exit()
    
    
# Pregunta 2

print("Responda la pregunta y ganara $333.333")

time.sleep(1)

print(pregunta2)
print(respuesta2)

opcion = str(input("Ingrese la opcion correcta : "))
if opcion == repuestas_letras[3]:
    premio += 333_333
    print("Gano la segunda pregunta!!!!!!")
else:
    print("Perdio el juego")
    exit()
    
# Pregunta 3

print("Responda la pregunta y ganara $333.333")

time.sleep(1)

print(pregunta3)
print(respuesta3)

opcion = str(input("Ingrese la opcion correcta : "))
if opcion == repuestas_letras[3]:
    premio += 333_334
    print("Gano la tercera pregunta!!!!!!")
else:
    print("Perdio el juego")
    exit()
    
    
print('El premio es: {:,.2f}'.format(premio))






# numero = 10000000000000000000



# print('NUmero: {:,.2f}'.format(numero))