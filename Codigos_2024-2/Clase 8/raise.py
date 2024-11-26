# # Definición del error personalizado
# class NoTerroristas(Exception):
#     def __init__(self, mensaje, codigo_error=None):
#         # Guarda el mensaje y el código de error
#         super().__init__(mensaje)
#         self.codigo_error = codigo_error

#     def __str__(self):
#         # Retorna el mensaje del error y el código si está presente
#         if self.codigo_error:
#             return f"[Error {self.codigo_error}]: {self.args[0]}"
#         else:
#             return self.args[0]





# import random


# generar_numero = random.randint(910,912)
# day = generar_numero

# avion = "Avion Comercial"


# if day == 911:
#     raise NameError()
#     print("Directo a torre")
# else:
#     print("Mejor otro dia, o el proximo")
    
    

"""
Piense en un numero, la maquina debe adivinarlo

Debe indicarle si el numero es mayor o menor al que penso

Debe tener un limite de intentos

Debe ingresar el rango de numeros a adivinar

Debe indicarle si el numero es correcto

Si el numero es correcto, debe indicarle cuantos intentos le tomo adivinarlo

Provocar un error si el numero es menor a 0

Provocar un error si el numero es mayor al rango

Provocar un error si el numero no es un numero

Provocar un error si el numero no es un entero





"""
import math
limites_superior = 100
limite_inferior = 0

intentos = 10

encontrado = False

while not encontrado:
    print("Indique si su numero es mayor o menor. \n 1. Menor \n 2. Mayor \n 3. Es ese numero!👌")
    nuevo_rango = math.floor((limites_superior + limite_inferior) / 2)
    if limite_inferior == limites_superior:
        print(f"Tu numero es {nuevo_rango}")
        encontrado = True
    print(nuevo_rango)
    opcion = int(input(": ")) 
    
    if opcion == 1:
        limite_inferior = nuevo_rango
    elif opcion == 2:
        limites_superior = nuevo_rango
    else:
        print("FELICITACIONES SOS TODO UN CRACKKKKKK")
        encontrado = True
    print(limite_inferior, limites_superior)
        
        
        
        