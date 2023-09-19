# """
# Ejemplo 1
# Funcion sin argumento y sin retorno

# """
# def saludar():
#     print("Hola Mundo")
    
# saludar() # Llamamos a la funcion saludar() y esta imprime "Hola Mundo"



# """
# Ejemplo 2
# Funcion con argumentos pero sin retorno

# """
# def concatenacion(texto1, texto2):
#     # En este caso la funcion recibe dos argumentos y los concatena.
#     print("Palabra unida: ", texto1, texto2)
    
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# concatenacion(nombre, apellido) # Llamamos a la funcion concatenacion() y 
#                                 #esta imprime "Palabra unida: nombre apellido"
                                
                                
                                
"""
Ejemplo 3
Funcion con argumentos y con retorno
"""

def suma(num1, num2):
    # En este caso la funcion recibe dos argumentos y los suma.
    return num1 + num2

operacion = suma(2,2)
operacion2 = suma(2,2) * suma(2,2) 

print(operacion)
print(operacion2)


"""
Ejemplo 4
Funcion sin argumentos y con retorno

"""
def funcion1():
    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    return (nombre, edad)

print(funcion1())