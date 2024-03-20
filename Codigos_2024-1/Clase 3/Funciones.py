# """

# Las funciones en python son un conjunto de instrucciones que realizan una tarea especifica, 
# estas funciones pueden recibir parametros y retornar valores.

# Para definir una funcion en python se utiliza la palabra reservada def seguida del nombre 
# de la funcion y los parametros que recibe.


























# """
# #! Funcion sin parametros, sin retorno. (Solo de acciones)
# def saludar():
#     print("Hola mundo")
    
    
    
    
    
    
    
    
    
    
    
    
# saludar()

# #! Funcion con parametros, sin retorno. (Solo de acciones)
# def saludar(nombre, edad):
#     print("Hola ", nombre, "Su edad es", edad)
    
# saludar("Juan",19)

# #* Funcion con parametros, con retorno. (Se espera un valor)

# def sumar(a, b):
#     return a + b

# resultado = sumar(5, 3)
# print(resultado)


#* Funcion sin parametros, con retorno. (Se espera un valor)

def obtener_datos():
    nombre = input("Ingrese su nombre : ")
    edad = int(input("Ingrese su edad : "))
    return nombre, edad

nombre1, edad1 = obtener_datos()

print(nombre1)
print(edad1)






