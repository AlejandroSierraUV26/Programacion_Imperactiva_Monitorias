"""
Existen diferentes metodos en python para manejar las listas.

- append: Agrega un elemento al final de la lista

- insert: Agrega un elemento en una posición específica

- remove: Elimina un elemento de la lista

- pop: Elimina un elemento de la lista en una posición específica

- clear: Elimina todos los elementos de la lista

- index: Devuelve la posición de un elemento en la lista

- count: Cuenta cuantas veces se repite un elemento en la lista

- sort: Ordena la lista

- reverse: Invierte la lista

"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# append

lista.append(11)
print(lista)

# insert

lista.insert(0, 0)
print(lista)

# remove

lista.remove(0)
print(lista)

# pop

lista.pop(0)
print(lista)

# clear

lista.clear()
print(lista)

# index

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista.index(5))

# count

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 5, 5]
print(lista.count(5))

# sort

lista.sort()
print(lista)

# reverse

lista.reverse()
print(lista)

# copy

lista2 = lista.copy()
print(lista2)

# extend

lista.extend([11, 12, 13])
print(lista)

"""
    Realizar un algortimo que realize lo mismo para:
    
    - count() --> Contar cuantas veces se repite un elemento en la lista
    - index() --> Devuelve la posición de un elemento en la lista
    - sort() --> Ordena la lista
    - reverse() --> Invierte la lista
    - copy() --> Copia la lista
    
    - aplicar una funcion a una lista. 
    Ejemplo:
    lista = [1, 2, 3, 4, 5] -> [1, 4, 9, 16, 25] {x^2}
    lista = [1, 2, 3, 4, 5] -> [2, 4, 6, 8, 10] {x*2}
    lista = [1, 2, 3, 4, 5] -> [1, 8, 27, 64, 125] {x^3}
    
    - max() --> Retorna el elemento mayor de la lista    
    - prom() --> Retorna el promedio de los elementos de la lista
    - min() --> Retorna el elemento menor de la lista
    
    
"""




