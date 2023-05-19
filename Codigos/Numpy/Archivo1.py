"""
Para aquellas personas que no lo sepan 
numpy no esta instalado predeterminado 
en python

Para eso usaremos el siguiente codigo en la terminal
Se puede hacer directamente desde el visual studio code

?Ctrl + ñ

el siguiente comando : 

*pip install numpy 

recuerden que deben de tener el python habilitado con el PATH
de otro modo no dejara instalar librerias externas.


"""

#Importamos numpy y lo nombramos a nuestro gusto con la palabra reservada "as" 
import numpy as np

#Opcion 1 
#Matriz 2x2 de 0
lista = np.array([[0,0],[0,0]])

#Opcion 2 
#Matriz 2x2 de 0 por numpy
#Los parametros deben ir en parentexis y dando su dimension
lista2 = np.zeros((2,3))


print(lista2)
