"""
    Realizar un algortimo que realize lo mismo para:
    
    - index() --> Devuelve la posición de un elemento en la lista
    - count() --> Contar cuantas veces se repite un elemento en la lista
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

def index(lista,numero):
    #* Buscar la posicion de un elemento si esta repetido.
    posiciones = []
    for i in range(0,len(lista)):
        if numero == lista[i]:
            posiciones.append(i)
    return posiciones
def count(lista,numero):
    #* Contar un elemento las veces que se repite
    contador = 0
    for i in range(0,len(lista)):
        if numero == lista[i]:
            contador+=1
    return contador
def sort(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def reverse(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def copy(lista):
    lista_nueva = []
    for i in range(0,len(lista)):
        lista_nueva.append(lista[i])
    return lista_nueva

def al_cuadrado(x):
    return x**2

def multiplicar_2(x):
    return x*2
def funcion_funcion(lista,funcion):
    for i in range(0,len(lista)):
        lista[i] = funcion(lista[i])
    return lista
def maximo(lista):
    mayor = lista[0]
    for i in range(0,len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            
    return mayor
lista1 = [1,2,3,4,5,6,7,8,9,1]
print(maximo(lista1))



