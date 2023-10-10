"""
Las expeciones en la programacion de la computadora 
son errores que se pueden presentar en el codigo,
estos errores pueden ser de dos tipos:
    - Errores de sintaxis
    - Errores de logica

Los errores de sintaxis son errores que se presentan
cuando el codigo no esta bien escrito, por ejemplo
cuando se escribe una palabra reservada de python
de manera incorrecta. 

Los errores de logica son errores que se presentan
cuando el codigo esta bien escrito pero no hace lo
que se quiere que haga, por ejemplo cuando se quiere
que el codigo sume dos numeros y en vez de eso los
multiplica.

Para manejar los errores de sintaxis se utiliza la
palabra reservada try y para manejar los errores de
logica se utiliza la palabra reservada assert.

La palabra reservada try se utiliza de la siguiente
manera:
    try:
        #Codigo
    except:
        #Codigo
    
La palabra reservada assert se utiliza de la siguiente
manera:
    assert #Condicion, "Mensaje de error"
    
Ejemplo:

try:
    assert 1 == 2, "1 no es igual a 2"
except:
    print("Error")
    
try:
    assert 1 == 1, "1 no es igual a 1"
except:
    print("Error")
        
"""
    

"""
Un ejemplo muy cotiadiano que sucede en la programacion, 
sucede durante la entrada de datos por consola.


- Situacion que se espera un numero entero y se ingresa una letra por error.

"""
# try: 
#     numero = int(input("Ingrese un numero : "))
# except:
#     print("Error, ingresa un numero entero")


"""
>>> Ingresa una letra.
"""
"""
Aunque la excepcion evita que ocurra el error, termina el codigo.
Cosa que podriamos evitar si le aplicamos un bucle.

"""

while(True):
    try: 
        numero = int(input("Ingrese un numero : "))
        # Si la persona ingresa un numero correcto debemos terminar el bucle.
        break
    except:
        print("Error, ingresa un numero entero")
        
"""
Aunque en python no es necesario espeficiar el error. Es una buena 
practica hacerlo.

Tener en cuenta los errores que existen.
"""
    

