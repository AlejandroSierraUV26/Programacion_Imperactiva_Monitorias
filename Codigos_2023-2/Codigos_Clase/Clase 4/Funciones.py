"""
Para definir un funcion en python hay dos tipos, aquellas que tienen un valor de retorno
y las que son vacias. 

Para definir una funcion se utiliza la palabra reservada def, seguido del nombre de la funcion

def nombre_funcion():

Para las funciones que tienen un valor de retorno, se utiliza la palabra reservada return

def nombre_funcion():
    return valor

Un ejemplo muy sencillo seria : 

def suma():
    return 2 + 2
    
Para llamar a una funcion se utiliza el nombre de la funcion seguido de parentesis

suma()

Para las funciones que no tienen un valor de retorno, se utiliza la palabra reservada pass

def nombre_funcion():
    pass
    
Ejemplo de la funcion:

def suma():
    print(2 + 2)
    
"""


# Ejemplo 1 
def suma_funcion():
    return 2 + 2

# Ejemplo 1 
print(suma_funcion())

# Ejemplo 2
def suma_funcion2():
    print(2 + 2)

# Ejemplo 2
suma_funcion2()    
