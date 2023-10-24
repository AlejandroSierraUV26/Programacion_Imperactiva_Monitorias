"""
Las listas en python es una estructura de datos que nos permite almacenar gran cantidad de valores,
estos valores pueden ser de cualquier tipo, incluso podemos almacenar listas dentro de listas.
Las listas son mutables, es decir, podemos modificarlas una vez creadas.

Las listas se definen con corchetes [] y los elementos separados por comas.

Ejemplo:

mi_lista = [1, 2, 3, 4, 5]

Para acceder a los elementos de una lista, se hace mediante su índice, el cual empieza en 0.

Ejemplo:

print(mi_lista[0])
# Salida: 1

Para modificar un elemento de la lista, se hace mediante su índice.

Ejemplo:


mi_lista[0] = 0

print(mi_lista)

# Salida: [0, 2, 3, 4, 5]


Existen diferentes metodos que nos permiten acceder a diferentes funcionalidades de las listas,
a continuación se muestran algunos de ellos.

"""

# Crear una lista de ejemplo

mi_lista = [1, 2, 3, 4, 5]

#? append(x): 
#! Agrega un elemento al final de la lista
mi_lista.append(8)
print(mi_lista)  
#* Salida: [1, 2, 3, 4, 5, 8]

#? extend(iterable): 
#! Agrega elemenos de un iterable al final de la lista
mi_lista.extend([9,10])
print(mi_lista)  
#* Salida: [1, 2, 3, 4, 5, 6, 9,10]

#? insert(i, x): 
#! Inserta un elemento en una posición específica
mi_lista.insert(2, 0)
print(mi_lista) 
#* Salida: [1, 2, 0, 3, 4, 5, 6, 7, 8]

#? remove(x): 
#! Elimina la primera aparición del elemento especificado
mi_lista.remove(3)
print(mi_lista)
#* Salida: [1, 2, 0, 4, 5, 6, 7, 8]

#? pop([i]): 
#! Elimina y devuelve el elemento en la posición especificada (o el último si no se especifica)
elemento_eliminado = mi_lista.pop(2)
print(elemento_eliminado)  
#* Salida: 0
print(mi_lista)  
#* Salida: [1, 2, 4, 5, 6, 7, 8]

#? index(x, start, end): 
#! Devuelve el índice de la primera aparición del elemento especificado en el rango especificado
indice = mi_lista.index(5)

print(indice)  
#* Salida: 3

#? count(x): 
#! Devuelve la cantidad de veces que un elemento aparece en la lista
conteo = mi_lista.count(5)
print(conteo)  
#* Salida: 1

#? sort(key=None, reverse=False): 
#! Ordena la lista en su lugar (por defecto en orden ascendente)
mi_lista.sort()
print(mi_lista)  
#* Salida: [1, 2, 4, 5, 6, 7, 8]

#? reverse(): 
#! Invierte el orden de los elementos en la lista
mi_lista.reverse()
print(mi_lista)  
#* Salida: [8, 7, 6, 5, 4, 2, 1]

#? copy(): 
#! Devuelve una copia superficial de la lista
copia = mi_lista.copy()
print(copia)

#? clear(): 
#! Elimina todos los elementos de la lista
mi_lista.clear()
print(mi_lista)  
#* Salida: []

#? len(lista): 
#! Devuelve la longitud de la lista
longitud = len(copia)
print(longitud)